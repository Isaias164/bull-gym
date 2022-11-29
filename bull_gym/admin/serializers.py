from rest_framework import serializers
from django.contrib.auth import get_user_model
from api.models import Reserbas,Gym,Futbol,Paddle,Sink
user = get_user_model()


class UsersSerializers(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = "__all__"
        
class BookingsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Reserbas
        fields = "__all__"

class SinksSerializers(serializers.ModelSerializer):
    class Meta:
        model = Sink
        fields = "__all__"
        
class GymSerializers(serializers.ModelSerializer):
    class Meta:
        model = Gym
        fields = "__all__"

class PaddleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Paddle
        fields = "__all__"
        
class FutbolSerializers(serializers.ModelSerializer):
    class Meta:
        model = Futbol
        fields = "__all__"