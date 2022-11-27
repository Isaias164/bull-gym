from rest_framework import serializers
from django.contrib.auth import authenticate, login
from rest_framework_simplejwt.tokens import RefreshToken
from api.models import Users
from django.contrib.auth.models import update_last_login
from django.contrib.auth import get_user_model

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
    
