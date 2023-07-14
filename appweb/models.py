from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profesional(models.Model):
  
    nombre = models.CharField(max_length=50)
    apellidoPaterno = models.CharField(max_length=50)
    rut = models.CharField(max_length=10)
    correo = models.EmailField()
    foto = models.ImageField(upload_to="profesional")
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, null=True)


    def nombre_completo(self):
        return "{} {}".format(self.nombre, self.apellidoPaterno)
    
    def __str__(self):
        return self.nombre_completo()
    

    
Motivo = [
    [0, "sugerencia"],
    [1, "Reclamo"],
    [2, "Felicitaciones"],
    [3, "Consulta"]
]

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    apellido_Paterno = models.CharField(max_length=50)
    rut = models.IntegerField()
    email = models.CharField(max_length=100)
    telefono = models.IntegerField()
    motivo = models.IntegerField(choices=Motivo)
    mensaje = models.TextField()

    def __str__(self):
        return self.nombre + " " + self.email
    
Categoria = [
    [0, "Electronica"],
    [1, "Cajas de Cambio"],
    [2, "Suspensión y Frenos"]
]


EstadoAtencion = [
    [0, "En Espera"],
    [1, "Aprobada"],
    [2, "Rechazada"]
]

 
class Atencion(models.Model):
    foto = models.ImageField(null=True)
    categoria = models.IntegerField(choices=Categoria)
    titulo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    mecanico = models.ForeignKey(Profesional, null=True, on_delete=models.CASCADE)
    estado = models.IntegerField(choices=EstadoAtencion, default=0)
    motivoRechazo = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.titulo
    
class TrabajaConNosotros(models.Model):
    foto = models.ImageField(null=True, default='default.png')
    nombres = models.CharField(max_length=100)
    apellidoPaterno = models.CharField(max_length=100, verbose_name='Apellido Paterno')
    apellidoMaterno = models.CharField(max_length=100, verbose_name='Apellido Materno')
    rut = models.IntegerField()
    fechaNacimiento = models.DateField(verbose_name='Fecha de nacimiento')
    correo = models.EmailField()
    telefono = models.IntegerField()
    informacion = models.TextField(max_length=500, verbose_name='Háblanos de ti')

    def __str__(self):
        return f"Postulación de: {self.nombres.title()}"



