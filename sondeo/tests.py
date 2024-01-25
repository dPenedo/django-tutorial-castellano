from django.test import TestCase
import datetime
from django.utils import timezone
from .models import Pregunta

class PreguntaModelTest(TestCase):
    def test_publicado_recientemenete_con_pregunta_futura(self):
        """
        publicado_recientemente() devuelve False para preguntas publicadas en el futuro
        """
        tiempo = timezone.now() + datetime.timedelta(days=30)
        pregunta_futura = Pregunta(fecha_de_publicacion=tiempo)
        self.assertIs(pregunta_futura.publicado_recientemente(), False)
    def test_publicado_recientemente_con_pregunta_reciente(self):
        """
        publicado_recientemente() devuelve True para preguntas con fecha_de_publicacion
        de los ultimos días
        """
        tiempo = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        pregunta_reciente = Pregunta(fecha_de_publicacion=tiempo)
        self.assertIs(pregunta_reciente.publicado_recientemente(), True)


