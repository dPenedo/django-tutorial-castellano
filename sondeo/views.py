from .models import Pregunta, Respuesta
from django.shortcuts import get_object_or_404, render


def index(request):
    lista_ultimas_preguntas = Pregunta.objects.order_by("-fecha_de_publicacion")[:5]
    context = {
        "lista_ultimas_preguntas": lista_ultimas_preguntas,
    }
    return render(request, "sondeo/index.html", context)

def detalle(request, pregunta_id):
    pregunta = get_object_or_404(Pregunta, pk=pregunta_id) 
    respuesta = pregunta.respuesta_set.all()
    return render(request, "sondeo/detalle.html", {"pregunta": pregunta, "respuesta": respuesta})


def resultados(request, pregunta_id):
    respuesta = "Estás viendo los resultados de la pregunta %s "
    return render(request, "sondeo/resultados.html", {"respuesta": respuesta})

def votar(request, pregunta_id):
    return render(request, "sondeo/votar.html", {"pregunta": pregunta})
    
