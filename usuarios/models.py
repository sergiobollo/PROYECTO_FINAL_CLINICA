from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_secretaria = models.BooleanField(default=False)
    is_medico = models.BooleanField(default=False)
    is_vendedor = models.BooleanField(default=False)
    is_taller = models.BooleanField(default=False)
    is_gerencia = models.BooleanField(default=False)

class Secretaria(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    
class Medico(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    
class Vendedor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    
class Taller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    
class Gerencia(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)