from django.contrib.auth.models import User
from django.contrib.auth import login, logout

from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView,ListAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from api.serializers import LoginSerializer, CreateUserSerializers, BookingsSerializers,AddBookingsSerializers
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
    queryset = Reserbas.objects.none()
    serializer_class = AddBookingsSerializers
    
    def get_context_data(self, **kwargs):
        context["request"] = self.request 
        return context
    
    
# Paddle
class BookingsPaddleViews(CreateAPIView):
    permission_classes = [IsAuthenticated,PermissionsPaddle]
    serializer_class = AddBookingsSerializers
    queryset = Reserbas.objects.all()

# Gym
class BookingsGymViews(CreateAPIView):
    permission_classes = [IsAuthenticated,PermissionsGym]
    serializer_class = AddBookingsSerializers
    queryset = Reserbas.objects.all()

# Fútbol
class BookingsFutbolViews(CreateAPIView):
    permission_classes = [IsAuthenticated,PermissionsFutbol]
    serializer_class = AddBookingsSerializers
    queryset = Reserbas.objects.all()


# class LogingViews(ViewSet):
#     permission_classes = [IsAuthenticated]

#     def destroy(self, request, pk=None):
#         """
#         Esta vista elimina la cuenta del usuario
#         """
#         Instalaciones.insertar(
#             request,
#             "CALL DECREMENTAR_RECERBAS_REALIZADAS_USUARIO(%s)",
#             (request.user.username,),
#         )
#         request.user.delete()
#         request.session.flush()
#         logout(request)
#         return Response(
#             {"error": False, "message": "cuenta elimnada satisfactoriamente"},
#             status=status.HTTP_202_ACCEPTED,
#             content_type="application/json",
#         )

#     def list(request):
#         data = {
#             "nombre": request.user.first_name + " " + request.user.last_name,
#             "usuario": request.user.username,
#             "email": request.user.email,
#             "fechaCreacion": request.user.date_joined,
#         }
#         return Response(
#             data=data, status=status.HTTP_200_OK, content_type="application/json"
#         )


# class EmailViews(ViewSet):
#     permission_classes = [IsAuthenticated]

#     def update(self, request):
#         datos = UpdateEmailSerializers(data=request.data)
#         data = "Correo actualizado correctamnte"
#         if not datos.is_valid():
#             return Response(data={"error": True, "message": "Este campo es requerido"})
#         estado = status.HTTP_205_RESET_CONTENT
#         try:
#             request.user.email = datos.validated_data["email"]
#             request.user.save()
#         except Exception as e:
#             data = "Ha ocurrido un error y no hemos podido actualizar tu correo"
#             print("Ocurrio el siguiente error")
#             estado = status.HTTP_400_BAD_REQUEST
#         finally:
#             return Response(data=data, status=estado, content_type="application/json")


# class PasswordViews(ViewSet):
#     permission_classes = [IsAuthenticated]

#     def update(self, request):
#         datos = UpdatePasswordSerializers(data=request.data)
#         if not datos.is_valid():
#             return Response(
#                 data={"error": True, "message": "Este campo es requerido"},
#                 status=status.HTTP_400_BAD_REQUEST,
#                 content_type="application/json",
#             )
#         if not datos.validated_data["password"] == datos.validated_data["password2"]:
#             return Response(
#                 data={"password": "Las contraseñas no coinciden"},
#                 content_type="application/json",
#                 status=status.HTTP_204_NO_CONTENT,
#             )

#         mensaje = """No se ha podido cambiar su contraseña.
#                         Vuelva a intentarlo más tarde"""
#         stado = status.HTTP_205_RESET_CONTENT
#         try:
#             from django.contrib.auth import update_session_auth_hash

#             request.user.set_password(datos.validated_data["password2"])
#             request.user.save()
#             update_session_auth_hash(request, request.user)
#             mensaje = "Se ha actualizado la contraseña correctamente"
#         except Exception as e:
#             stado = status.HTTP_400_BAD_REQUEST
#             print(f"error {str(e)}")
#         finally:
#             return Response(data=mensaje, content_type="application/json", status=stado)


# class Recerbas(ViewSet):
#     def create(self, request):
#         datos = DeportesSerializers(data=request.data)
#         if not datos.is_valid():
#             return Response(
#                 data={"error": "Datos json mal enviados"},
#                 content_type="application/json",
#                 status=status.HTTP_400_BAD_REQUEST,
#             )
#         try:
#             deporte = datos.validated_data["deporte"].lower()
#             resp = ""
#             stado = status.HTTP_200_OK
#             # si la solicitud tiene una clve deporte y esa clave deporte es gym
#             if deporte == "gym":
#                 from .models import Gym

#                 # import el modelo y obtengo los datos del objeto user. Lo mismo hago lo mismo en lo demas elif
#                 resp = Gym.insertar(
#                     self,
#                     "SELECT INSERTAR_CLIENTE_GYM(%s,%s,%s,%s,%s,%s,%s)",
#                     (
#                         1,
#                         request.user.first_name,
#                         request.user.last_name,
#                         request.user.username,
#                         deporte,
#                         datos.validated_data["fecha"],
#                         datos.validated_data["hora"],
#                     ),
#                 )
#             elif deporte == "pileta":
#                 from .models import Pileta

#                 resp = Pileta.insertar(
#                     self,
#                     "SELECT INSERTAR_CLIENTE_PILETA(%s,%s,%s,%s,%s,%s,%s)",
#                     (
#                         1,
#                         request.user.first_name,
#                         request.user.last_name,
#                         request.user.username,
#                         deporte,
#                         datos.validated_data["fecha"],
#                         datos.validated_data["hora"],
#                     ),
#                 )
#             elif deporte == "futbol":
#                 from .models import CanchasFutbol

#                 resp = CanchasFutbol.insertar(
#                     self,
#                     "SELECT INSERTAR_CLIENTE_FUTBOL(%s,%s,%s,%s,%s,%s,%s)",
#                     (
#                         1,
#                         request.user.first_name,
#                         request.user.last_name,
#                         request.user.username,
#                         deporte,
#                         datos.validated_data["fecha"],
#                         datos.validated_data["hora"],
#                     ),
#                 )
#             elif deporte == "paddle":
#                 from .models import CanchasPaddle

#                 resp = CanchasPaddle.insertar(
#                     self,
#                     "SELECT INSERTAR_CLIENTE_PADDLE(%s,%s,%s,%s,%s,%s,%s)",
#                     (
#                         1,
#                         request.user.first_name,
#                         request.user.last_name,
#                         request.user.username,
#                         deporte,
#                         datos.validated_data["fecha"],
#                         datos.validated_data["hora"],
#                     ),
#                 )
#             else:
#                 resp = "NO HAS SELECCIONADO UN DEPORTE. POR FAVOR SELECIONA UN DEPORTE".upper()
#                 stado = status.HTTP_203_NON_AUTHORITATIVE_INFORMATION
#         except Exception as obj:
#             stado = status.HTTP_400_BAD_REQUEST
#             print("ha ocurrido el siguiente error: " + str(obj))
#         finally:
#             return Response(data=resp, content_type="application/json", status=stado)

#     def retrieve(self, request, pk=None):
#         idCliente = GruposReserbas.eliminarRecerbaModels(self, pk)
#         return Response(
#             data={"mensaje": "Recerva eliminada"},
#             content_type="application/json",
#             status=status.HTTP_200_OK,
#         )

#     def list(self, request):
#         from .models import GruposReserbas

#         listaRecerbas = GruposReserbas.listar(self, request.user.username)
#         listaRecerbas = self.formatearDatos(request, listaRecerbas)
#         return Response(
#             data={"recerbas": listaRecerbas},
#             status=status.HTTP_200_OK,
#             content_type="application/json",
#         )
