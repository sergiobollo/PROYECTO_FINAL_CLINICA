from django.contrib.auth.models import AbstractUser
from django.db import models
import datetime

class User(AbstractUser):
    is_secretaria = models.BooleanField(default=False)
    is_medico = models.BooleanField(default=False)
    is_vendedor = models.BooleanField(default=False)
    is_taller = models.BooleanField(default=False)
    is_gerencia = models.BooleanField(default=False)
