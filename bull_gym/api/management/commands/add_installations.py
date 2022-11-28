from django.core.management.base import BaseCommand
from api.models import Gym,Sink,Futbol,Paddle
from colorama import init,Fore,Back

class Command(BaseCommand):

    def handle(self, *args, **options):
        init()
        gym = Gym.objects.create(price=700,maximum_capacity=15,name="gym_1")
        print(Back.BLACK + Fore.GREEN+"Se agrego la instalación Gym")
        pileta = Sink.objects.create(price=1200,maximum_capacity=20,name="sink_1")
        print(Back.BLACK + Fore.GREEN+"Se agrego la instalación Pileta1")
        pileta2 = Sink.objects.create(price=1200,maximum_capacity=20,name="sink_2")
        print(Back.BLACK + Fore.GREEN+"Se agrego la instalación  Pileta2")
        paddle1 = Paddle.objects.create(price=500,maximum_capacity=2,name="cancha_1")
        print(Back.BLACK + Fore.GREEN+"Se agrego la instalación Paddle1")
        paddle2 = Paddle.objects.create(price=500,maximum_capacity=2,name="cancha_2")
        print(Back.BLACK + Fore.GREEN+"Se agrego la instalación Paddle2")
        futbol1 = Futbol.objects.create(price=1000,maximum_capacity=10,name="cancha_1")
        print(Back.BLACK + Fore.GREEN+"Se agrego la instalación Fútbol1")
        futbol2 = Futbol.objects.create(price=1000,maximum_capacity=10,name="cancha_2")
        print(Back.BLACK + Fore.GREEN+"Se agrego la instalación Fútbol1")
        futbol3 = Futbol.objects.create(price=1000,maximum_capacity=10,name="cancha_3")
        print(Back.BLACK + Fore.GREEN+"Se agrego la instalación Fútbol1")
        