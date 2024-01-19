from django.urls import path
from . import views


app_name = "sondeo"
urlpatterns = [
        # /sondeo/
        path("", views.index, name="index"),
        # Por ejemplo /sondeo/5/
        path("<int:pregunta_id>/", views.detalle, name="detalle"),
        # Por ejemplo /sondeo/resultados/
        path("<int:pregunta_id>/resultados/", views.resultados, name="resultados"),
        # Por ejemplo /sondeo/votar/
        path("<int:pregunta_id>/votar/", views.votar, name="votar"),
        ]
