from django.db import models

class Medico(models.Model):
    username = models.CharField(max_length=64)
    nombre = models.CharField(max_length=64)
    apellido = models.CharField(max_length=64)
    especialidad = models.CharField(max_length=64)
  
    def __str__(self):
        return f"{self.nombre} {self.apellido} {self.especialidad}"
    
class AsistenciaTurno(models.Model):
    nombre = models.CharField(max_length=64)
    
    def __str__(self):
        return f"{self.nombre}"
   
class Paciente(models.Model):
    nombre = models.CharField(max_length=64)
    apellido = models.CharField(max_length=64)
    medico = models.ForeignKey(Medico, on_delete=models.RESTRICT, related_name="medico_asignado")
  
    def __str__(self):
        return f"{self.nombre} {self.apellido}"   
          
class Turno(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.RESTRICT, related_name="paciente_turno")
    medico =  models.ForeignKey(Medico, on_delete=models.RESTRICT, related_name="medico_turno")
    dia = models.DateField()
    hora = models.TimeField()
    asistio = models.ForeignKey(AsistenciaTurno, on_delete=models.RESTRICT, related_name="asistencia_turno", default = "1")
    
    def __str__(self):
        return f" {self.paciente} {self.dia} {self.hora} {self.medico} {self.asistio}"
    
class HistorialMedico(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.RESTRICT, related_name="paciente_historial")
    medico =  models.ForeignKey(Medico, on_delete=models.RESTRICT, related_name="medico_historial")
    observacion = models.TextField()
    fecha_y_hora = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return f"{self.paciente} {self.medico} {self.fecha_y_hora} {self.observacion}"
    
class IzquierdaDerecha(models.Model):
    izquierda_derecha = models.CharField(max_length=64)
    
    def __str__(self):
        return f" {self.izquierda_derecha}"
    
class LejosCerca(models.Model):
    lejos_cerca = models.CharField(max_length=64)
    
    def __str__(self):
        return f" {self.lejos_cerca}"
    
class Armazon(models.Model):
    armazon = models.CharField(max_length=64)
    
    def __str__(self):
        return f" {self.armazon}"
    
class Producto(models.Model):
    nombre_producto = models.CharField(max_length=64)
    precio = models.DecimalField(decimal_places=2, max_digits=5)
    lejos_cerca = models.ForeignKey(LejosCerca, on_delete=models.RESTRICT, related_name="lejos_o_cerca")
    izquierda_derecha = models.ForeignKey(IzquierdaDerecha, on_delete=models.RESTRICT, related_name="izquierda_o_derecha")
    armazon = models.ForeignKey(Armazon, on_delete=models.RESTRICT, related_name="incluye_armazon")
    
    def __str__(self):
        return f" {self.nombre_producto}"
    
class FormaDePago(models.Model):
    nombre = models.CharField(max_length=64)
  
    def __str__(self):
        return f"{self.nombre}"
    
class EstadoPedido(models.Model):
    nombre = models.CharField(max_length=64)
  
    def __str__(self):
        return f"{self.nombre}" 
    
class Pedido(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.RESTRICT, related_name="paciente_producto")
    producto = models.ForeignKey(Producto, on_delete=models.RESTRICT, related_name="producto_pedido")
    cantidad = models.IntegerField()
    subtotal = models.DecimalField(decimal_places=2, max_digits=10)
    tipo_de_pago = models.ForeignKey(FormaDePago, on_delete=models.RESTRICT, related_name="forma_de_pago")
    estado = models.ForeignKey(EstadoPedido, on_delete=models.RESTRICT, related_name="estado_de_pedido", default='1')
    fecha_y_hora = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.paciente} {self.producto} {self.cantidad} {self.subtotal} {self.fecha_y_hora} {self.tipo_de_pago} {self.estado}"
