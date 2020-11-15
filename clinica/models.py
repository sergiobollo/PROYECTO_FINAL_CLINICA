from django.db import models

class Medico(models.Model):
    nombre = models.CharField(max_length=64)
    apellido = models.CharField(max_length=64)
    especialidad = models.CharField(max_length=64)
  
    def __str__(self):
        return f"{self.nombre} {self.apellido} {self.especialidad}"  
   
class Paciente(models.Model):
    nombre = models.CharField(max_length=64)
    apellido = models.CharField(max_length=64)
  
    def __str__(self):
        return f"{self.nombre} {self.apellido}"   
          
class Turno(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.RESTRICT, related_name="paciente_turno")
    medico =  models.ForeignKey(Medico, on_delete=models.RESTRICT, related_name="medico_turno")
    dia = models.DateField()
    hora = models.TimeField()
    
    def __str__(self):
        return f"{self.paciente} {self.dia} {self.hora} {self.medico}"
    
class HistorialMedico(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.RESTRICT, related_name="paciente_historial")
    medico =  models.ForeignKey(Medico, on_delete=models.RESTRICT, related_name="medico_historial")
    observacion = models.TextField()
    fecha_y_hora = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return f"{self.paciente} {self.medico} {self.fecha_y_hora} {self.observacion}"
    
class Producto(models.Model):
    nombre_producto = models.CharField(max_length=64)
    precio = models.DecimalField(decimal_places=2, max_digits=5)
    lente = models.CharField(max_length=64)
    armazon = models.CharField(max_length=64)
    
    def __str__(self):
        return f" {self.nombre_producto}"
    
class FormaDePago(models.Model):
    nombre = models.CharField(max_length=64)
  
    def __str__(self):
        return f"{self.nombre}"  
    
class Pedido(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.RESTRICT, related_name="paciente_producto")
    producto = models.ForeignKey(Producto, on_delete=models.RESTRICT, related_name="producto_pedido")
    cantidad = models.IntegerField()
    subtotal = models.DecimalField(decimal_places=2, max_digits=10)
    tipo_de_pago = models.ForeignKey(FormaDePago, on_delete=models.RESTRICT, related_name="forma_de_pago", default="1")
    estado = models.CharField(max_length=64)
    fecha_y_hora = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.paciente} {self.producto} {self.cantidad} {self.subtotal} {self.fecha_y_hora} {self.tipo_de_pago} {self.estado}"
