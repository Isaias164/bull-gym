from rest_framework.permissions import BasePermission
from api.models import Gym,Sink,Futbol,Paddle

class PermissionsSink(BasePermission):
    def has_permission(self, request, view):
        return Sink.objects.filter(has_capacity=True).exists() 
    
class PermissionsPaddle(BasePermission):
    def has_permission(self, request, view):
        return Paddle.objects.filter(has_capacity=True).exists()

class PermissionsFutbol(BasePermission):
    def has_permission(self, request, view):
        return Futbol.objects.filter(has_capacity=True).exists()

class PermissionsGym(BasePermission):
    def has_permission(self, request, view):
        return Gym.objects.filter(has_capacity=True).exists()