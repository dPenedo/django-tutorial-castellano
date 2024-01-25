from django.urls import path
from . import views


app_name = "sondeo"
urlpatterns = [
        # /sondeo/
        path("", views.IndexView.as_view(), name="index"),
        # Por ejemplo /sondeo/5/
        path("<int:pk>/", views.DetalleView.as_view(), name="detalle"),
        # Por ejemplo /sondeo/resultados/
        path("<int:pk>/resultados/", views.ResultadosView.as_view(), name="resultados"),
        # Por ejemplo /sondeo/votar/
        path("<int:pregunta_id>/votar/", views.votar, name="votar"),
        ]
