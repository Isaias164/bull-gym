from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from api.models import Reserbas
from admin.serializers import *
from django.contrib.auth import get_user_model
from admin.permissions import AdminUser

user = get_user_model()
    
class UsersViews(ListAPIView):
    permission_classes = [IsAuthenticated,AdminUser]
    queryset = user.objects.all()
    serializer_class = UsersSerializers
    
    
class BookingsViews(ListAPIView):
    permission_classes = [IsAuthenticated,AdminUser]
    queryset = Reserbas.objects.all()
    serializer_class = BookingsSerializers