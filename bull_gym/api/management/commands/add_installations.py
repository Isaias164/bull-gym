from django.core.management.base import BaseCommand
from api.models import Gym,Pileta,CanchasFutbol,CanchasPaddle
from colorama import init,Fore,Back

class Command(BaseCommand):

    def handle(self, *args, **options):
        init()
        gym = Gym.objects.create(precio=700,cantidadUsuarios=15)
        print(Back.BLACK + Fore.GREEN+"Se agrego la instalación Gym")
        pileta = Pileta.objects.create(precio=1200,cantidadUsuarios=20)
        print(Back.BLACK + Fore.GREEN+"Se agrego la instalación Pileta1")
        pileta2 = Pileta.objects.create(precio=1200,cantidadUsuarios=20)
        print(Back.BLACK + Fore.GREEN+"Se agrego la instalación  Pileta2")
        paddle1 = CanchasPaddle.objects.create(precio=500,cantidadUsuarios=2)
        print(Back.BLACK + Fore.GREEN+"Se agrego la instalación Paddle1")
        paddle2 = CanchasPaddle.objects.create(precio=500,cantidadUsuarios=2)
        print(Back.BLACK + Fore.GREEN+"Se agrego la instalación Paddle2")
        futbol1 = CanchasFutbol.objects.create(precio=1000,cantidadUsuarios=10)
        print(Back.BLACK + Fore.GREEN+"Se agrego la instalación Fútbol1")
        futbol2 = CanchasFutbol.objects.create(precio=1000,cantidadUsuarios=10)
        print(Back.BLACK + Fore.GREEN+"Se agrego la instalación Fútbol1")
        futbol3 = CanchasFutbol.objects.create(precio=1000,cantidadUsuarios=10)
        print(Back.BLACK + Fore.GREEN+"Se agrego la instalación Fútbol1")
        