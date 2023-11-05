from django.urls import path
from .views import (
    VistaListaMetodos,
    VistaDetalleMetodo,
    VistaFiltroMetodos
)

urlpatterns = [
    path("", VistaListaMetodos.as_view(), name="inicio"),
    path("<int:pk>/", VistaDetalleMetodo.as_view(), name="detalle_metodo"),
    path("<str:filtro>", VistaFiltroMetodos.as_view(), name="filtro_metodo")
]
