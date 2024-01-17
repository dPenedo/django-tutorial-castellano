from .models import Pregunta
from django.shortcuts import render




def index(request):
    lista_ultimas_preguntas = Pregunta.objects.order_by("-fecha_de_publicacion")[:5]
    context = {
        "lista_ultimas_preguntas": lista_ultimas_preguntas,
    }
    return render(request, "sondeo/index.html", context)

def detalle(request, pregunta_id):
    pregunta = get_object_or_404(Pregunta, pk=pregunta_id) 
    return render(request, "sondeo/detalle.html", {"pregunta": pregunta})


def resultados(request, pregunta_id):
    respuesta = "Estás viendo los resultados de la pregunta %s "
    return HttpResponse(respuesta % pregunta_id)

def votar(request, pregunta_id):
    return HttpResponse("Estás votando a la pregunta %s." % pregunta_id)
    
