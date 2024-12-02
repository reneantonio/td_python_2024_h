from django.db import models

class Hotel(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    calificacion = models.DecimalField(max_digits=3, decimal_places=1)
    cant_votos = models.IntegerField()
    direccion = models.CharField(max_length=255) 
    def __str__(self):
        return self.nombre

class Comentario(models.Model):
    hotel = models.ForeignKey(Hotel, related_name="comentarios", on_delete=models.CASCADE)
    nombre_usuario = models.CharField(max_length=255)
    comentario = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentario de {self.nombre_usuario} para {self.hotel.nombre}"

class Atributo():
    nombre = models.CharField(max_length=255)  


class Atributo_Hotel():
    hotel = models.ForeignKey(Hotel, related_name="atributos", on_delete=models.CASCADE)
    atributo = models.ForeignKey(Atributo, related_name="atributos_hoteles", on_delete=models.CASCADE)
    valor_atributo = models.CharField(max_length=255)

    def __str__(self):
        return f"Atributo {self.atributo.nombre} para {self.hotel.nombre} con valor {self.valor_atributo}"

