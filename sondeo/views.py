from django.http import HttpResponseRedirect
from .models import Pregunta, Respuesta
from django.urls import reverse
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
    pregunta = get_object_or_404(Pregunta, pk=pregunta_id)
    return render(request, "sondeo/resultados.html", {"pregunta": pregunta})

def votar(request, pregunta_id):
    pregunta = get_object_or_404(Pregunta, pk=pregunta_id) 
    try:
        respuesta_seleccionada =  pregunta.respuesta_set.get(pk=request.POST["respuesta"])
    except (KeyError, Respuesta.DoesNotExist):
        # Volver a mostrar el formulario de respuesta
        return render(request, "sondeo/detalle.html", {"pregunta": pregunta, "error_message": "No as seleccionado una respuesta"})
    else:
        respuesta_seleccionada.votos += 1
        respuesta_seleccionada.save()
        # Devuelve siempre un HttpResponseRedirect después de manejar exitosamente los datos POST. 
        # Esto previene que haya información posteada dos veces si un usario presiona el botón Atrás
        return HttpResponseRedirect(reverse("sondeo:resultados", args=(pregunta.id,)))


