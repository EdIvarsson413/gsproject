from django.urls import path
from .views import (
    VistaListaMetodos,
    VistaDetalleMetodo,
    VistaFiltroMetodos,
    VistaFiltrosDinamicos
)

urlpatterns = [
    path("", VistaListaMetodos.as_view(), name="inicio"),
    path("<uuid:pk>/", VistaDetalleMetodo.as_view(), name="detalle_metodo"),
    path("<str:filtro>", VistaFiltroMetodos.as_view(), name="filtro_metodo"),
    path("filtro-dinamico/<str:variable>/<str:filtro>", VistaFiltrosDinamicos.as_view() , name ="filtro_dinamico")
]
