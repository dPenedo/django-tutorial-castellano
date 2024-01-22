import datetime

from django.db import models
from django.utils import timezone


class Pregunta(models.Model):
    texto_pregunta = models.CharField(max_length=200) # Tamaño máximo del texto
    fecha_de_publicacion = models.DateTimeField("fecha de publicación") # Con el argumento "decha de publicación" se le añade un texto legible para las personas, si no sería el que esté por defecto "fecha_de_publicacion" en este caso
    def __str__(self):
        return self.texto_pregunta # Devuelve el texto de la pregunta al convertir el objeto a cadena de texto
    def publicado_recientemente(self):
        return self.fecha_de_publicacion >= timezone.now() - datetime.timedelta(days = 1) 


class Respuesta(models.Model):
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE) # Relación de clave foránea con la tabla Pregunta y al borrarse se borran las respuestas asociadas
    texto_elegido = models.CharField(max_length=200)
    votos = models.IntegerField(default=0) #Número de votos. Empìeza en 0
    def __str__(self):
        return self.texto_elegido

# Create your models here.
