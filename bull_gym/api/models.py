from django.db import models
from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):
    user_name = models.CharField(max_length=15)
    password = models.CharField(max_length=130)
    email = models.EmailField(unique=True)
    
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS =  []
