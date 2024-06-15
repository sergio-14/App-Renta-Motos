
from django.db import models

class Nacionalidad(models.Model):
    nacionalidad_id = models.AutoField(primary_key=True)
    nacionalidad = models.CharField(max_length=100)

    def __str__(self):
        return self.nacionalidad

class Cliente(models.Model):
    ndi = models.CharField(max_length=20, primary_key=True)
    nombres = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50)
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=200)
    nacionalidad = models.ForeignKey(Nacionalidad, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombres} {self.apellido_paterno} {self.apellido_materno}"

class TipoMoto(models.Model):
    tipo_id = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=100)

    def __str__(self):
        return self.tipo

class Moto(models.Model):
    DISPONIBILIDAD_CHOICES = [
        ('disponible', 'Disponible'),
        ('ocupado', 'Ocupado'),
    ]

    moto_id = models.AutoField(primary_key=True)
    placa = models.CharField(max_length=20)
    color = models.CharField(max_length=30)
    tipo = models.ForeignKey(TipoMoto, on_delete=models.CASCADE)
    modelo = models.CharField(max_length=50)
    detalle = models.TextField()
    tarifa = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=10, choices=DISPONIBILIDAD_CHOICES, default='disponible')
    foto = models.ImageField(upload_to='motos_fotos/', null=True, blank=True)

    def __str__(self):
        return f"{self.placa} - {self.modelo}"

class Alquiler(models.Model):
    DISPONIBILIDAD_CHOICES = [
        ('disponible', 'Disponible'),
        ('ocupado', 'Ocupado'),
    ]

    alquiler_id = models.AutoField(primary_key=True)
    fecha = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    cantidad_horas = models.IntegerField()
    estado = models.CharField(max_length=10, choices=DISPONIBILIDAD_CHOICES, default='disponible')
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    moto = models.ForeignKey(Moto, on_delete=models.CASCADE)

    def __str__(self):
        return f"Alquiler {self.alquiler_id} - {self.cliente} - {self.moto}"

