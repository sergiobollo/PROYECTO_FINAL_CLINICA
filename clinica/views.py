from django.shortcuts import render
from .models import Medico, Paciente, Turno, HistorialMedico, Producto, Pedido, FormaDePago, LejosCerca, IzquierdaDerecha, Armazon, EstadoPedido, AsistenciaTurno, Vendedor
from django.http import HttpResponseBadRequest, HttpResponseRedirect, Http404
from django.urls import reverse
from django import forms
from django.utils.translation import get_language, activate
from datetime import datetime, timedelta
from django.template.defaultfilters import date
import calendar, locale

# Create your views here.

def index(request):
    return render(request,"clinica/index.html", {
        })
    
def turnos(request):
    fecha =""
    if request.method == "POST":
        form = FormFiltroFecha(request.POST)
        if form.is_valid():
            dia = form.cleaned_data["filtrar_turnos_por_dia"]
            fecha = dia.dia
    if request.user.is_secretaria:
        if fecha:
            turnos = Turno.objects.filter(dia=fecha)
        else:
            turnos = Turno.objects.all()
    else:
        usuario = request.user.username
        try:
            medico = Medico.objects.get(username=usuario)
        except Medico.DoesNotExist:
            raise Http404("No se encontro medico")
        if fecha:
            turnos = Turno.objects.filter(medico=medico).filter(dia=fecha)
        else:
            turnos = Turno.objects.filter(medico=medico)
    return render(request,"clinica/turnos.html", {
        "titulo": "Turnos asignados a pacientes",
        "turnos": turnos,
        "form": FormFiltroFecha}
        )
    
class FormFiltroFecha(forms.Form):
    filtrar_turnos_por_dia = forms.ModelChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), queryset=Turno.objects.all())
    
def asistencia_paciente_turno(request):
    ahora = datetime.now()
    turnos = Turno.objects.filter(asistio = "2")
    if request.method == "POST":
        form = FormFiltroSemanaMes(request.POST)
        if form.is_valid():
            lapso = form.cleaned_data["lapso"]
            if lapso == "0":
                semana = timedelta(weeks=1)
                fecha = ahora - semana
                turnos = Turno.objects.filter(asistio = "2").filter(dia__range=(fecha, ahora))
                return render(request, "clinica/asistencia_paciente_turno.html", {"turnos": turnos,
                                                                      "form": form,
                                                                      "mensaje": "Ultima semana:"})
            else:
                mes = timedelta(weeks=4)
                fecha = ahora - mes
                turnos = Turno.objects.filter(asistio = "2").filter(dia__range=(fecha, ahora))
                return render(request, "clinica/asistencia_paciente_turno.html", {"turnos": turnos,
                                                                      "form": form,
                                                                      "mensaje": "Ultimo mes:"})
        else:
            return render(request, "clinica/asistencia_paciente_turno.html", {"turnos": turnos,
                                                                      "form": form})
    return render(request, "clinica/asistencia_paciente_turno.html", {"turnos": turnos,
                                                                      "form": FormFiltroSemanaMes})

def ausencia_paciente_turno(request):
    ahora = datetime.now()
    turnos = Turno.objects.filter(asistio = "3")
    if request.method == "POST":
        form = FormFiltroSemanaMes(request.POST)
        if form.is_valid():
            lapso = form.cleaned_data["lapso"]
            if lapso == "0":
                semana = timedelta(weeks=1)
                fecha = ahora - semana
                turnos = Turno.objects.filter(asistio = "3").filter(dia__range=(fecha, ahora))
                return render(request, "clinica/ausencia_paciente_turno.html", {"turnos": turnos,
                                                                      "form": form,
                                                                      "mensaje": "Ultima semana:"})
            else:
                mes = timedelta(weeks=4)
                fecha = ahora - mes
                turnos = Turno.objects.filter(asistio = "3").filter(dia__range=(fecha, ahora))
                return render(request, "clinica/ausencia_paciente_turno.html", {"turnos": turnos,
                                                                      "form": form,
                                                                      "mensaje": "Ultimo mes:"})
        else:
            return render(request, "clinica/ausencia_paciente_turno.html", {"turnos": turnos,
                                                                      "form": form})
    return render(request, "clinica/ausencia_paciente_turno.html", {"turnos": turnos,
                                                                      "form": FormFiltroSemanaMes})

class FormFiltroSemanaMes(forms.Form):
    c = [("0", "Ultima semana"), ("1","Ultimo mes")]
    lapso= forms.ChoiceField(choices=c)
    
def pacientes(request):
    usuario = request.user.username
    try:
        medico = Medico.objects.get(username=usuario)
    except Medico.DoesNotExist:
        raise Http404("No se encontro medico")
    pacientes = Paciente.objects.filter(medico=medico)    
    return render(request,"clinica/pacientes.html", {
        "titulo": "Historial medico por paciente",
        "pacientes": pacientes,
        "medico": medico
        })
    
def historial_medico(request, paciente_id):
    paciente = Paciente.objects.get(id=paciente_id)
    try:
        historial_medico = HistorialMedico.objects.filter(paciente=paciente_id)
    except HistorialMedico.DoesNotExist:
        raise Http404("No se encontryó paciente")
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
    ahora = datetime.now()
    pedidos= Pedido.objects.all()
    if request.method == "POST":
        form = FormFiltroSemanaMes(request.POST)
        if form.is_valid():
            lapso = form.cleaned_data["lapso"]
            if lapso == "0":
                semana = timedelta(weeks=1)
                fecha = ahora - semana
                pedidos = Pedido.objects.filter(fecha_y_hora__range=(fecha, ahora))
                return render(request, "clinica/pedidos.html", {"titulo": "Listado de pedidos por paciente",
                                                                "pedidos": pedidos,
                                                                      "form": form,
                                                                      "mensaje": "Ultima semana:"})
            else:
                mes = timedelta(weeks=4)
                fecha = ahora - mes
                pedidos = Pedido.objects.filter(fecha_y_hora__range=(fecha, ahora))
                return render(request, "clinica/pedidos.html", {"titulo": "Listado de pedidos por paciente",
                                                                "pedidos": pedidos,
                                                                      "form": form,
                                                                      "mensaje": "Ultimo mes:"})
        else:
            return render(request, "clinica/pedidos.html", {"turnos": turnos,
                                                                      "form": form})
    return render(request,"clinica/pedidos.html", {
        "titulo": "Listado de pedidos por paciente",
        "pedidos": pedidos,
        "form": FormFiltroSemanaMes
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
                            subtotal = subtotal)
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
    cantidad = forms.IntegerField(label="Cantidad", min_value=0, max_value=100)
    tipo_de_pago = forms.ModelChoiceField(queryset = FormaDePago.objects.all())

def editar_pedido_vendedor (request):
    if request.method == "POST":
        form = FormUpdatePedidoVendedor(request.POST)
        if form.is_valid():
            pedido = form.cleaned_data["pedido"]
            estado = form.cleaned_data["estado"]
            id = pedido.id
            Pedido.objects.filter(id=id).update(estado=estado)
            return HttpResponseRedirect(reverse("clinica:pedidos"))
        else:
            return render(request, "clinica/editar_pedido_vendedor.html", {
                "form": form
                })
    
    return render(request, "clinica/editar_pedido_vendedor.html", {
        "form": FormUpdatePedidoVendedor()
    })
    
class FormUpdatePedidoVendedor(forms.Form):
    pedido = forms.ModelChoiceField(queryset = Pedido.objects.all())
    estado = forms.ModelChoiceField(queryset = EstadoPedido.objects.exclude(nombre = "Finalizado"))
    
def editar_pedido_taller (request):
    if request.method == "POST":
        form = FormUpdatePedidoTaller(request.POST)
        if form.is_valid():
            pedido = form.cleaned_data["pedido"]
            estado = form.cleaned_data["estado"]
            id = pedido.id
            Pedido.objects.filter(id=id).update(estado=estado)
            return HttpResponseRedirect(reverse("clinica:pedidos"))
        else:
            return render(request, "clinica/editar_pedido_taller.html", {
                "form": form
                })
    
    return render(request, "clinica/editar_pedido_taller.html", {
        "form": FormUpdatePedidoTaller()
    })
    
class FormUpdatePedidoTaller(forms.Form):
    pedido = forms.ModelChoiceField(queryset = Pedido.objects.all())
    estado = forms.ModelChoiceField(queryset = EstadoPedido.objects.filter(nombre = "Finalizado"))
    
def cargar_producto(request):
    if request.method == "POST":
        form = FormNuevoProducto(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data["nombre_producto"]
            precio = form.cleaned_data["precio_producto"]
            lejos_cerca= LejosCerca.objects.get(id=1)
            izquierda_derecha= IzquierdaDerecha.objects.get(id=1)
            armazon= Armazon.objects.get(id=1)
            producto = Producto(nombre_producto=nombre,
                            precio=precio,
                            lejos_cerca= lejos_cerca,
                            izquierda_derecha=izquierda_derecha,
                            armazon=armazon)
            producto.save()
            return HttpResponseRedirect(reverse("clinica:productos"))
        else:
            return render(request, "clinica/cargar_producto.html", {
                "form": form
                })
    
    return render(request, "clinica/cargar_producto.html", {
        "form": FormNuevoProducto()
    })
    
class FormNuevoProducto(forms.Form):
    nombre_producto = forms.CharField(max_length=64)
    precio_producto = forms.DecimalField(decimal_places=2, max_digits=5, min_value=0)
    
def cargar_producto_lente(request):
    if request.method == "POST":
        form = FormNuevoProductoLente(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data["nombre_lente"]
            precio = form.cleaned_data["precio_lente"]
            lejos_o_cerca = form.cleaned_data["lejos_o_cerca"]
            izquierda_o_derecha = form.cleaned_data["izquierda_o_derecha"]
            armazon = form.cleaned_data["armazon"]
            pedido = Producto(nombre_producto=nombre,
                            precio=precio,
                            lejos_cerca = lejos_o_cerca,
                            izquierda_derecha = izquierda_o_derecha,
                            armazon= armazon)
            pedido.save()
            return HttpResponseRedirect(reverse("clinica:productos"))
        else:
            return render(request, "clinica/cargar_producto_lente.html", {
                "form": form
                })
    
    return render(request, "clinica/cargar_producto_lente.html", {
        "form": FormNuevoProductoLente()
    })
        
class FormNuevoProductoLente(forms.Form):
    nombre_lente = forms.CharField(max_length=64, label="Nombre lente")
    precio_lente = forms.DecimalField(decimal_places=2, max_digits=5, min_value=0)
    lejos_o_cerca = forms.ModelChoiceField(queryset = LejosCerca.objects.all())
    izquierda_o_derecha = forms.ModelChoiceField(queryset=IzquierdaDerecha.objects.all())
    armazon = forms.ModelChoiceField(queryset= Armazon.objects.all())

def crear_paciente(request):
    if request.method == "POST":
        form = FormCrearPaciente(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data["nombre"]
            apellido = form.cleaned_data["apellido"]
            medico = form.cleaned_data["medico_asignado"]
            paciente = Paciente(nombre=nombre,
                            apellido = apellido,
                            medico = medico)
            paciente.save()
            return HttpResponseRedirect(reverse("usuarios:index"))
        else:
            return render(request, "clinica/crear_paciente.html", {
                "form": form
                })
    return render(request, "clinica/crear_paciente.html", {"form": FormCrearPaciente})

class FormCrearPaciente(forms.Form):
    nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=64, label ="Nombre")
    apellido = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=64, label ="Apellido")
    medico_asignado = forms.ModelChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), queryset = Medico.objects.all())
    
class FormGenerarTurno(forms.Form):
    paciente = forms.ModelChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), queryset = Paciente.objects.all())
    dia = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control'}))
    hora = forms.TimeField(widget=forms.TimeInput(attrs={'class': 'form-control'}))

def generar_turno(request):
    if request.method == "POST":
        form = FormGenerarTurno(request.POST)
        if form.is_valid():
            paciente = form.cleaned_data["paciente"]
            medico_object = paciente.medico
            medico_id = medico_object.id
            try:
                medico = Medico.objects.get(id = medico_id)
            except Medico.DoesNotExist:
                raise Http404("No se encontro medico")            
            dia = form.cleaned_data["dia"]
            hora = form.cleaned_data["hora"]
            turno = Turno(paciente=paciente,
                            medico = medico,
                            dia = dia,
                            hora = hora)
            turno.save()
            return HttpResponseRedirect(reverse("clinica:turnos"))
        else:
            return render(request, "clinica/generar_turno.html", {
                "form": form
                })
    return render(request, "clinica/generar_turno.html", {"form": FormGenerarTurno})

class FormGenerarTurno(forms.Form):
    paciente = forms.ModelChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), queryset = Paciente.objects.all())
    dia = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control'}))
    hora = forms.TimeField(widget=forms.TimeInput(attrs={'class': 'form-control'}))
    
def comentario_medico(request):
    if request.method == "POST":
        form = FormComentarMedico(request.POST)
        if form.is_valid():
            medico_user = request.user.username
            try:
                medico = Medico.objects.get(username = medico_user)
            except Medico.DoesNotExist:
                raise Http404("No se encontro medico")   
            paciente = form.cleaned_data["paciente"]
            comentario = form.cleaned_data["observacion"]
            historial_medico = HistorialMedico(observacion = comentario,
                                               medico = medico,
                                               paciente = paciente)
            historial_medico.save()
            return HttpResponseRedirect(reverse("clinica:pacientes"))
        else:
            return render(request, "clinica/comentario_medico.html", {
                "form": form
                })
    return render(request, "clinica/comentario_medico.html", {"form": FormComentarMedico})

class FormComentarMedico(forms.Form):
    paciente = forms.ModelChoiceField(queryset = Paciente.objects.all())
    observacion = forms.CharField()

def productos_mas_vendidos(request):
    productos = Producto.objects.all()
    cant_max1 = 0
    cant_max2 = 0
    ahora = datetime.now()
    mes = timedelta(weeks=4)
    fecha = ahora - mes
    for prod in productos:
        pedidos_prod= Pedido.objects.filter(producto = prod.id).filter(fecha_y_hora__range=(fecha, ahora))
        cantidad_prod = 0
        for ped in pedidos_prod:
            cantidad_prod = cantidad_prod + ped.cantidad
        if cantidad_prod > cant_max1:
            prod_max1 = prod.nombre_producto
            cant_max1= cantidad_prod
        elif cantidad_prod > cant_max2:
            prod_max2 = prod.nombre_producto
            cant_max2= cantidad_prod
    return render(request, "clinica/productos_mas_vendidos.html", {"cant_max1": cant_max1,
                                                                   "cant_max2": cant_max2,
                                                                   "prod_max1": prod_max1,
                                                                   "prod_max2": prod_max2})
    
def total_vendedor(request):
    vendedores = Vendedor.objects.all()
    vendedores_ventas = []
    today = datetime.now()
    año = today.year
    for vend in vendedores:
        for m in range(12):
            mes = m+1
            cantidad_ventas = Pedido.objects.filter(vendedor = vend).filter(fecha_y_hora__year__gte=año,
                                 fecha_y_hora__month__gte=mes,
                                 fecha_y_hora__year__lte=año,
                                 fecha_y_hora__month__lte=mes).count()
            mes_nombre = calendar.month_name[mes] 
            vendedor_ventas = (vend, cantidad_ventas, mes_nombre)
            vendedores_ventas.append(vendedor_ventas)
    print(vendedor_ventas)
    return render(request, "clinica/total_vendedor.html", {"ventas": vendedores_ventas})