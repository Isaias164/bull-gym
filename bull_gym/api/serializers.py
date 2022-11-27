from rest_framework import serializers
from django.contrib.auth import authenticate, login
from rest_framework_simplejwt.tokens import RefreshToken
from api.models import Users


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def verify_login(self, validate_data):
        request = self.context.get("request")
        validate_data.update({"username": validate_data.pop("email")})
        user = authenticate(request, **validate_data)
        if not user:
            return {"error": True, "message": "Usuario y/o contraseña incorrecta"}

        refresh = RefreshToken.for_user(user)
        login(request, user)
        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }


class CreateUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = Users
        exclude = ["id", "is_manager"]
