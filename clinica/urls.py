from django.urls import path
from . import views

app_name = "clinica"
urlpatterns = [
    path("", views.index, name = "index"),
    path("turnos", views.turnos, name = "turnos"),
    path("pacientes", views.pacientes, name = "pacientes"),
    path("<int:paciente_id>", views.historial_medico, name = "historial_medico"),
    
]