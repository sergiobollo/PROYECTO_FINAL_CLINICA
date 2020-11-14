from django.shortcuts import render
from .models import Medico, Paciente, Turno, HistorialMedico, Producto, Pedido
from django.http import HttpResponseBadRequest, HttpResponseRedirect, Http404

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
    
def turnos(request):
    return render(request,"clinica/turnos.html", {
        "titulo": "Gestión de turnos",
        "turnos": Turno.objects.all()
        })
    
def pacientes(request):
    return render(request,"clinica/pacientes.html", {
        "titulo": "Listado de pacientes",
        "pacientes": Paciente.objects.all(),
        })
    
def historial_medico(request, paciente_id):
    paciente = Paciente.objects.get(id=paciente_id)
    try:
        historial_medico = HistorialMedico.objects.filter(paciente=paciente_id)
    except HistorialMedico.DoesNotExist:
        raise Http404("No se encontroó paciente")
    return render(request,"clinica/historial_medico.html", {
        "historial_medico": historial_medico,
        "paciente": paciente
        })