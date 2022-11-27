from django.db import models
from django.contrib.auth.models import AbstractUser
from api.constants import TypePayments


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
    precio = models.IntegerField()
    cantidadUsuarios = models.IntegerField(blank=True, null=True)

    class Meta:
        abstract = True


class Gym(Instalaciones):
    class Meta:
        db_table = "gym"


class Pileta(Instalaciones):
    def __str__(self) -> str:
        return "Pileta " + str(self.id)

    class Meta:
        db_table = "pileta"


class CanchasFutbol(Instalaciones):
    def __str__(self) -> str:
        return "Cancha de fútbol " + str(self.id)

    class Meta:
        db_table = "canchasfutbol"


class CanchasPaddle(Instalaciones):
    def __str__(self) -> str:
        return "Cancha de paddle " + str(self.id)

    class Meta:
        db_table = "canchaspaddle"


class Reserbas(models.Model):
    time = models.IntegerField()
    date = models.DateField()
    sport = models.CharField(max_length=15)
    count = models.IntegerField()
    paid_payment = models.CharField(
        max_length=12, default=TypePayments.OWES, choices=TypePayments.choices
    )
    total_to_pay = models.IntegerField()
    futbol = models.ForeignKey(
        CanchasFutbol,
        db_column="futbol",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        db_constraint="reserba_futbol",
    )
    paddle = models.ForeignKey(
        CanchasPaddle,
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
        Pileta,
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
