from django.shortcuts import render
from .models import Medico, Paciente, Turno, HistorialMedico, Producto, Pedido

# Create your views here.

def index(request):
    return render(request,"clinica/index.html", {
        "titulo": "Bienvenidos a nuestra clínica de Optometría",
        "medicos": Medico.objects.all(),
        "pacientes": Paciente.objects.all(),
        "turnos": Turno.objects.all(),
        "historiales_medicos": HistorialMedico.objects.all(),
        "productos": Producto.objects.all(),
        "pedidos": Pedido.objects.all()
        })