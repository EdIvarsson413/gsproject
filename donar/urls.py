from django.urls import path
from .views import ( VistaIngresarDonatvo, VistaListaDonadores )

urlpatterns = [
    path( 'donar/', VistaIngresarDonatvo.as_view(), name = 'donar' ),
    path( 'donadores/', VistaListaDonadores.as_view(), name = 'donadores' )
]
