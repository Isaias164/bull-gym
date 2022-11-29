from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from api.models import Reserbas,Sink,Gym,Paddle,Futbol
from admin.serializers import *
from django.contrib.auth import get_user_model
from admin.permissions import AdminUser
from drf_multiple_model.views import FlatMultipleModelAPIView
from admin.pagination import LimitPagination

user = get_user_model()
    
class UsersViews(ListAPIView):
    permission_classes = [IsAuthenticated,AdminUser]
    queryset = user.objects.all()
    serializer_class = UsersSerializers
    
    
class BookingsViews(ListAPIView):
    permission_classes = [IsAuthenticated,AdminUser]
    queryset = Reserbas.objects.all()
    serializer_class = BookingsSerializers
    
    
class SinksViews(ListAPIView):
    permission_classes = [IsAuthenticated,AdminUser]
    queryset = Sink.objects.all()
    serializer_class = SinksSerializers
    
class PaddleViews(ListAPIView):
    permission_classes = [IsAuthenticated,AdminUser]
    queryset = Paddle.objects.all()
    serializer_class = PaddleSerializers
    
class FutbolViews(ListAPIView):
    permission_classes = [IsAuthenticated,AdminUser]
    queryset = Futbol.objects.all()
    serializer_class = FutbolSerializers
    
class GymViews(ListAPIView):
    permission_classes = [IsAuthenticated,AdminUser]
    queryset = Gym.objects.all()
    serializer_class = GymSerializers
    
class BookingsUsers(ListAPIView):
    permission_classes = [IsAuthenticated,AdminUser]
    serializer_class = BookingsUserSerializers
    
    def get_queryset(self):
        return Reserbas.objects.filter(user=self.request.query_params.get("id")) 
    
    


class BookingsFreeView(FlatMultipleModelAPIView):
    pagination_class = LimitPagination
    querylist = [
        {
            'queryset': Sink.objects.filter(has_capacity=True),
            'serializer_class': SinksSerializers,
            'label': 'sink',
        },
        {
            'queryset': Gym.objects.filter(has_capacity=True),
            'serializer_class': GymSerializers,
            'label': 'gym'
        },
        {
            'queryset': Paddle.objects.filter(has_capacity=True),
            'serializer_class': PaddleSerializers,
            'label': 'paddle',
        },
        {
            'queryset': Futbol.objects.filter(has_capacity=True),
            'serializer_class': FutbolSerializers,
            'label': 'futbol'
        },
        
    ]