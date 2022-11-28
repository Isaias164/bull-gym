from django.db.models import TextChoices


class TypePayments(TextChoices):
    PAYMENT = "Payment", ("Payment")
    OWES = "Owes", ("Owes")