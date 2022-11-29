from rest_framework import serializers
from django.contrib.auth import get_user_model
from api.models import Reserbas,Gym,Futbol,Paddle,Sink
user = get_user_model()


class AdminUsersSerializers(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = "__all__"
        
class AdminBookingsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Reserbas
        fields = "__all__"

class AdminSinksSerializers(serializers.ModelSerializer):
    class Meta:
        model = Sink
        fields = "__all__"
        
class AdminGymSerializers(serializers.ModelSerializer):
    class Meta:
        model = Gym
        fields = "__all__"

class AdminPaddleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Paddle
        fields = "__all__"
        
class AdminFutbolSerializers(serializers.ModelSerializer):
    class Meta:
        model = Futbol
        fields = "__all__"
        
class AdminUsersDeptSerializers(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ["name","last_name"]

class AdminBookingsUserSerializers(serializers.ModelSerializer):
    user = AdminUsersDeptSerializers(read_only=True)
    class Meta:
        model = Reserbas
        fields = ["date","time","sport","user"]
        depth = 1