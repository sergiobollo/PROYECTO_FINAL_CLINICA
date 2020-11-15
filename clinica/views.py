from django.shortcuts import render
from .models import Medico, Paciente, Turno, HistorialMedico, Producto, Pedido, FormaDePago
from django.http import HttpResponseBadRequest, HttpResponseRedirect, Http404
from django.urls import reverse
from django import forms

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
    
def productos(request):
    return render(request,"clinica/productos.html", {
        "titulo": "Productos",
        "productos": Producto.objects.all()
        })
    
def pedidos(request):
    return render(request,"clinica/pedidos.html", {
        "titulo": "Pedidos",
        "pedidos": Pedido.objects.all()
        })

def hacer_pedido(request):
    if request.method == "POST":
        form = FormNuevoPedido(request.POST)
        if form.is_valid():
            paciente = form.cleaned_data["paciente"]
            cantidad = form.cleaned_data["cantidad"]
            tipo_de_pago = form.cleaned_data["tipo_de_pago"]
            producto = form.cleaned_data["producto"]
            precio = producto.precio
            subtotal = precio * cantidad
            pedido = Pedido(paciente=paciente,
                            producto=producto,
                            cantidad = cantidad,
                            tipo_de_pago= tipo_de_pago,
                            estado = "Pendiente",
                            subtotal = subtotal)
            print(paciente)
            print(pedido)
            pedido.save()
            return HttpResponseRedirect(reverse("clinica:pedidos"))
        else:
            return render(request, "clinica/nuevo_pedido.html", {
                "form": form
                })
    
    return render(request, "clinica/hacer_pedido.html", {
        "form": FormNuevoPedido()
    })

class FormNuevoPedido(forms.Form):
    paciente = forms.ModelChoiceField(queryset = Paciente.objects.all())
    producto = forms.ModelChoiceField(queryset = Producto.objects.all())
    cantidad = forms.IntegerField(label="Cantidad")
    tipo_de_pago = forms.ModelChoiceField(queryset = FormaDePago.objects.all())
    
"""def update_db_field(name,field,value):
       MyModel.objects.get(name=name).update(field=value)"""