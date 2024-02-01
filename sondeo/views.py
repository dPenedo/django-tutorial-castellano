from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Pregunta, Respuesta


class IndexView(generic.ListView):
    template_name = "sondeo/index.html"
    context_object_name = "lista_ultimas_preguntas"

    def get_queryset(self):
        # Devuelve las ultimas 5 preguntas publicadas (sin incluir las que se publicarán en el futuro)
        return Pregunta.objects.filter(fecha_de_publicacion__lte=timezone.now()).order_by("-fecha_de_publicacion")[:5]

class DetalleView(generic.DetailView):
    model = Pregunta
    template_name = "sondeo/detalle.html"
    
class ResultadosView(generic.DetailView):
    model = Pregunta
    template_name = "sondeo/resultados.html"

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


