from django.contrib import admin
from .models import Medico, Paciente, Turno, HistorialMedico, Producto, Pedido

# Register your models here.
admin.site.register(Medico)
admin.site.register(Paciente)
admin.site.register(Turno)
admin.site.register(HistorialMedico)
admin.site.register(Producto)
admin.site.register(Pedido)