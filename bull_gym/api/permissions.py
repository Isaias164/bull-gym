from rest_framework.permissions import BasePermission
from api.models import Gym,Sink,Futbol,Paddle

class PermissionsSink(BasePermission):
    def has_permission(self, request, view):
        PermissionsSink.message = "Lo sentimos, de momento no tenemos más lugar para reserbar"
        return Sink.objects.filter(has_capacity=True).exists()
    
class PermissionsPaddle(BasePermission):
    def has_permission(self, request, view):
        PermissionsSink.message = "Lo sentimos, de momento no tenemos más lugar para reserbar"
        return Paddle.objects.filter(has_capacity=True).exists()

class PermissionsFutbol(BasePermission):
    def has_permission(self, request, view):
        PermissionsSink.message = "Lo sentimos, de momento no tenemos más lugar para reserbar"
        return Futbol.objects.filter(has_capacity=True).exists()

class PermissionsGym(BasePermission):
    def has_permission(self, request, view):
        PermissionsSink.message = "Lo sentimos, de momento no tenemos más lugar para reserbar"
        return Gym.objects.filter(has_capacity=True).exists()