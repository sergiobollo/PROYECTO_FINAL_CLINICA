from django.contrib import admin
from .models import Medico, Paciente, Turno, HistorialMedico, Producto, Pedido, FormaDePago, IzquierdaDerecha, LejosCerca, Armazon, EstadoPedido, AsistenciaTurno

# Register your models here.
admin.site.register(Medico)
admin.site.register(Paciente)
admin.site.register(Turno)
admin.site.register(HistorialMedico)
admin.site.register(Producto)
admin.site.register(Pedido)
admin.site.register(FormaDePago)
admin.site.register(IzquierdaDerecha)
admin.site.register(LejosCerca)
admin.site.register(Armazon)
admin.site.register(EstadoPedido)
admin.site.register(AsistenciaTurno)
