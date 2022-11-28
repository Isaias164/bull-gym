from django.db import models
from django.contrib.auth.models import AbstractUser
from api.constants import TypePayments,Sports


class Users(AbstractUser):
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=130)
    email = models.EmailField(unique=True)
    # datos personales
    name = models.CharField(max_length=20, null=True)
    last_name = models.CharField(max_length=20, null=True)

    is_manager = models.BooleanField(default=False)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


class Instalaciones(models.Model):
    price = models.IntegerField(default=0)
    maximum_capacity = models.IntegerField(blank=True, null=True)
    limit_users = models.IntegerField(default=0)
    has_capacity = models.BooleanField(default=True)
    name = models.CharField(max_length=15,null=True)
    class Meta:
        abstract = True


class Gym(Instalaciones):
    class Meta:
        db_table = "gym"


class Sink(Instalaciones):
    def __str__(self) -> str:
        return "Pileta " + str(self.id)

    class Meta:
        db_table = "sink"


class Futbol(Instalaciones):
    def __str__(self) -> str:
        return "Cancha de fútbol " + str(self.id)

    class Meta:
        db_table = "futbol"


class Paddle(Instalaciones):
    def __str__(self) -> str:
        return "Cancha de paddle " + str(self.id)

    class Meta:
        db_table = "paddle"
        
        
class Reserbas(models.Model):
    time = models.IntegerField(null=True)
    date = models.DateField(auto_now_add=True)
    sport = models.CharField(max_length=15)
    # count = models.IntegerField(null=True)
    paid_payment = models.CharField(
        max_length=12, default=TypePayments.OWES, choices=TypePayments.choices
    )
    total_to_pay = models.IntegerField(null=True,default=0)
    user = models.ForeignKey(
        Users,
        db_column="user",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        db_constraint="reserbas_user",
    )
    futbol = models.ForeignKey(
        Futbol,
        db_column="futbol",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        db_constraint="reserba_futbol",
    )
    paddle = models.ForeignKey(
        Paddle,
        db_column="paddle",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        db_constraint="reserba_paddle",
    )
    gym = models.ForeignKey(
        Gym,
        db_column="gym",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        db_constraint="reserba_gym",
    )
    pileta = models.ForeignKey(
        Sink,
        db_column="pileta",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        db_constraint="reserba_pileta",
    )

    def listar(self, params1):
        from django.db import connection

        query = "SELECT * FROM lista_recerbas_usuario WHERE username = %s;"
        resp = ""
        with connection.cursor() as cursor:
            try:
                cursor.execute(query, (params1,))
                resp = cursor.fetchall()
            except Exception as objStr:
                resp = str(objStr)
        return resp

    def eliminarRecerbaModels(self, id):
        from django.db import connection

        query = "SELECT BORRAR_CLIENTE(%s);"
        resp = ""
        with connection.cursor() as cursor:
            try:
                cursor.execute(query, (id,))
                resp = cursor.fetchone()
            except Exception as objStr:
                resp = str(objStr)
        return resp

    class Meta:
        db_table = "gruposreserbas"
        ordering = ["date"]
        verbose_name_plural = "Grupo de Recerbas"
