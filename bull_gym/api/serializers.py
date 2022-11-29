from rest_framework import serializers
from django.contrib.auth import authenticate, login
from rest_framework_simplejwt.tokens import RefreshToken
from api.models import Users
from django.contrib.auth.models import update_last_login
from django.contrib.auth import get_user_model
from api.models import Reserbas,Gym,Sink,Paddle,Futbol
from datetime import date
from django.db.models import Q
user = get_user_model()

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def verify_login(self, validate_data):
        request = self.context.get("request")
        _user = authenticate(request, **validate_data)
        if not _user:
            return {"error": True, "message": "Usuario y/o contraseña incorrecta"}

        update_last_login(user, _user)
        refresh = RefreshToken.for_user(_user)
        login(request, _user)
        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }
        

class CreateUserSerializers(serializers.Serializer):
    username = serializers.CharField()
    name = serializers.CharField()
    last_name = serializers.CharField()
    login = LoginSerializer()
    
    def create(self, validated_data):
        l = validated_data.pop("login")
        d = {"name":validated_data.get("name"),"last_name":validated_data.get("last_name"),"username":validated_data.get("username")} | dict(l)
        _user = user.objects.create(**d)
        _user.set_password(d.get("password"))
        _user.save()
        d = LoginSerializer(data=l,context={"request":self.context.get("request")})
        return d.verify_login(l)
    
    def validate_login(self,value):
        if user.objects.filter(email=value.get("email")).first():
            raise serializers.ValidationError("El email ya se encuentra registrado")
        return value        
    

class BookingsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Reserbas
        fields = ["date","time","total_to_pay","sport"]
        
        
class AddBookingsSerializers(serializers.Serializer):    
    time = serializers.IntegerField(min_value=9,max_value=22)
    date = serializers.DateField()
    sport = serializers.CharField()
    
    def create(self, validated_data):
        #today = date.today()
        today = validated_data.get("date")
        sport = validated_data.pop("sport").lower()
        request = self.context.get("request")
        
        obj = None
        validated_data.update({"user":request.user})
        match sport:
            case "paddle":
                paddle = Paddle.objects.filter(has_capacity=True)[0]
                obj = paddle
                validated_data.update({"paddle":paddle})
            case "gym":
                gym = Gym.objects.filter(has_capacity=True)[0]
                obj = gym
                validated_data.update({"gym":gym})
            case "sink":
                sink = Sink.objects.filter(has_capacity=True)[0]
                obj = sink
                validated_data.update({"pileta":sink})
            case "futbol":
                futbol = Futbol.objects.filter(has_capacity=True)[0]
                obj = futbol
                validated_data.update({"futbol":futbol})
        
        bookings,created = Reserbas.objects.get_or_create(**validated_data)
        if created:
            bookings.total_to_pay += obj.price
            bookings.sport = obj.name
            bookings.save()
            obj.limit_users += 1
            obj.save(update_fields=["limit_users"])
            if obj.cant_current_users == obj.maximum_capacity:
                obj.has_capacity = False
                obj.save(update_fields=["has_capacity"])
        else:
            raise serializers.ValidationError({"message":"Ya tenes registrado una reserba en este dia y horario"})
        
        return bookings
        
    def validate_sport(self, value):
        match value.lower():
            case "paddle":
                return value
            case "gym":
                return value
            case "sink":
                return value
            case "futbol":
                return value
            case _:
                raise serializers.ValidationError("No tenemos esta instalación")
    
    
class BookingsTotalPaySerializers(serializers.ModelSerializer):
    class Meta:
        model = Reserbas
        fields = ["date","time","total_to_pay"]