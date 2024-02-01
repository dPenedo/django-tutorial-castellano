from django.test import TestCase
import datetime
from django.utils import timezone
from django.urls import reverse
from .models import Pregunta



def crear_pregunta(texto_pregunta, days):
    """
    Crear una pregunta con el "texto_pregunta" dado y publicarlo con unos "dias" de diferencia (negativo para el pasado y positivo para el futuro)
    """
    tiempo = timezone.now() + datetime.timedelta(days=days)
    return Pregunta.objects.create(texto_pregunta=texto_pregunta, fecha_de_publicacion=tiempo)


class PruebasVistaIndicePreguntas(TestCase):
    def test_sin_preguntas(self):
        """
        Si no hay preguntas, se mostrará un mensaje apropiado
        """
        respuesta = self.client.get(reverse("sondeo:index"))
        self.assertEqual(respuesta.status_code, 200)
        self.assertContains(respuesta, "No hay sondeos disponibles")
        self.assertQuerySetEqual(respuesta.context["lista_ultimas_preguntas"], [])

    def test_pregunta_pasada(self):
        """
        Preguntas con fecha_de_publicacion del pasado son mostradas en la página del index
        """
        pregunta = crear_pregunta(texto_pregunta="Pregunta pasada.", days=-30)
        respuesta = self.client.get(reverse("sondeo:index"))
        self.assertQuerySetEqual(
            respuesta.context["lista_ultimas_preguntas"],
            [pregunta],
        )

    def test_pregunta_futura(self):
        """
        Pregunta con fecha_de_publicacion a futuro no son mostradas en la página de index
        """
        crear_pregunta(texto_pregunta="Pregunta futura", days=30)
        respuesta = self.client.get(reverse("sondeo:index"))
        self.assertContains(respuesta, "No hay sondeos disponibles")
        self.assertQuerySetEqual(respuesta.context["lista_ultimas_preguntas"], [])

    def test_preguntas_futuras_y_pasadas(self):
        """
        Aún si existen preguntas futuras o pasadas, solo se mostrarán las preguntas pasadas
        """
        pregunta = crear_pregunta(texto_pregunta="Pregunta pasada", days=-30)
        crear_pregunta(texto_pregunta="Pregunta futura", days=30)
        respuesta = self.client.get(reverse("sondeo:index"))
        self.assertQuerySetEqual(
            respuesta.context["lista_ultimas_preguntas"],
            [pregunta],
        )

    def test_dos_preguntas_pasadas(self):
        """
        Las preguntas de la página index pueden mostrar múltiples preguntas
        """
        pregunta1 = crear_pregunta(texto_pregunta="Pregunta pasada 1.", days=-30)
        pregunta2 = crear_pregunta(texto_pregunta="Pregunta pasada 2.", days=-5)
        respuesta = self.client.get(reverse("sondeo:index"))
        self.assertQuerySetEqual(
            respuesta.context["lista_ultimas_preguntas"],
            [pregunta2, pregunta1]
        )







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


