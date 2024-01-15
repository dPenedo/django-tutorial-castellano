from django.http import HttpResponse


def index(request):
    return HttpResponse("Hola mundo. Estás en el indice del sondeo")
# Create your views here.
