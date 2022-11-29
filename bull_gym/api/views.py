from django.contrib.auth.models import User
from django.contrib.auth import login, logout

from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView,ListAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from api.serializers import LoginSerializer, CreateUserSerializers, BookingsSerializers,AddBookingsSerializers, BookingsTotalPaySerializers
from api.models import Reserbas
from api.permissions import *

class LoginViews(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        data = LoginSerializer(data=request.data, context={"request": request})
        if data.is_valid(raise_exception=True):
            _auth = data.verify_login(data.validated_data)
            return Response(_auth)


class CreateUserViews(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        data = CreateUserSerializers(data=request.data,context={"request": request})
        if data.is_valid(raise_exception=True):
            t = data.create(data.validated_data)
            return Response(t)
        
class BookingsListViews(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BookingsSerializers
    
    def get_queryset(self):
        return Reserbas.objects.filter(user=self.request.user)
        
# Pileta        
class BookingsPiletaViews(CreateAPIView):
    permission_classes = [IsAuthenticated,PermissionsSink]
    serializer_class = AddBookingsSerializers
    queryset = Reserbas.objects.all()
     
    def get_context_data(self, **kwargs):
        context["request"] = self.request 
        return context

# Paddle
class BookingsPaddleViews(CreateAPIView):
    permission_classes = [IsAuthenticated,PermissionsPaddle]
    serializer_class = AddBookingsSerializers
    queryset = Reserbas.objects.all()
    
    def get_context_data(self, **kwargs):
        context["request"] = self.request 
        return context

# Gym
class BookingsGymViews(CreateAPIView):
    permission_classes = [IsAuthenticated,PermissionsGym]
    serializer_class = AddBookingsSerializers
    queryset = Reserbas.objects.all()

    def get_context_data(self, **kwargs):
        context["request"] = self.request 
        return context
# Fútbol
class BookingsFutbolViews(CreateAPIView):
    permission_classes = [IsAuthenticated,PermissionsFutbol]
    serializer_class = AddBookingsSerializers
    queryset = Reserbas.objects.all()

    def get_context_data(self, **kwargs):
        context["request"] = self.request 
        return context
    
class BookingsTotalPayViews(ListAPIView):
    serializer_class = BookingsTotalPaySerializers
    queryset = Reserbas.objects.all()