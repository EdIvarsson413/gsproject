from django.urls import path
from .views import (
    VistaCrearMetodo, 
    VistaListaMetodosReportados, 
    VistaDetalleMetodoNuevo,
    VistaEliminarMetodo,
    DescargarDatos
)

urlpatterns = [
    path('nuevo-metodo/', VistaCrearMetodo.as_view(), name = 'nuevo_metodo'),
    path('metodos-reportados/', VistaListaMetodosReportados.as_view(), name = 'metodos_nuevos'),
    path('ver-reporte/<int:pk>', VistaDetalleMetodoNuevo.as_view(), name = 'detalle_nuevo'),
    path('descargar/<int:pk>', DescargarDatos.as_view(), name = 'descarga'),
    path('eliminar/<int:pk>', VistaEliminarMetodo.as_view(), name = 'eliminar')
]
