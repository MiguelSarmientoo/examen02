from django.db import models

class Autor(models.Model):
    id_autor = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    id_libro = models.AutoField(primary_key=True)
    codigo = models.IntegerField()
    titulo = models.CharField(max_length=100)
    isbn = models.CharField(max_length=30)
    editorial = models.CharField(max_length=60)
    num_pags = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.titulo

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    num_usuario = models.IntegerField()
    nif = models.CharField(max_length=20)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

class Prestamo(models.Model):
    id_prestamo = models.AutoField(primary_key=True)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, blank=True, null=True)
    fecha_prestamo = models.DateTimeField()
    fecha_devolucion = models.DateTimeField()
    finalizado = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Prestamo {self.id_prestamo}"
