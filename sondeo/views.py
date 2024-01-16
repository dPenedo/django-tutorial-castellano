from django.http import HttpResponse
from django.template import loader
from .models import Pregunta



def index(request):
    lista_ultimas_preguntas = Pregunta.objects.order_by("-fecha_de_publicacion")[:5]
    template = loader.get_template("sondeo/index.html")
    context = {
        "lista_ultimas_preguntas": lista_ultimas_preguntas,
    }
    return HttpResponse(template.render(context, request))

def detalle(request, pregunta_id):
    return HttpResponse("Estás viendo la pregunta %s." % pregunta_id)

def resultados(request, pregunta_id):
    respuesta = "Estás viendo los resultados de la pregunta %s "
    return HttpResponse(respuesta % pregunta_id)

def votar(request, pregunta_id):
    return HttpResponse("Estás votando a la pregunta %s." % pregunta_id)
    
