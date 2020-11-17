from django.urls import path
from . import views

app_name = "clinica"
urlpatterns = [
    path("", views.index, name = "index"),
    path("turnos", views.turnos, name = "turnos"),
    path("pacientes", views.pacientes, name = "pacientes"),
    path("<int:paciente_id>", views.historial_medico, name = "historial_medico"),
    path("productos", views.productos, name = "productos"),
    path("pedidos", views.pedidos, name = "pedidos"),
    path("hacer_pedido", views.hacer_pedido, name = "hacer_pedido"),
    path("cargar_producto", views.cargar_producto, name = "cargar_producto"),
    path("cargar_producto_lente", views.cargar_producto_lente, name = "cargar_producto_lente"),
    path("crear_paciente", views.crear_paciente, name="crear_paciente"),
    path("generar_turno", views.generar_turno, name="generar_turno"),
    path("comentario_medico", views.comentario_medico, name ="comentario_medico")
]