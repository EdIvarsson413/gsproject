from django.shortcuts import render
from django.views.generic import CreateView, ListView
from .models import Donativo
from django.urls import reverse_lazy
from django.shortcuts import redirect

# Create your views here.
class VistaIngresarDonatvo(CreateView):
    model = Donativo
    template_name = 'donar/crear_donativo.html'
    fields = ( "cantidad", )

    def form_valid(self, form):
        form.instance.donador = self.request.user
        return super().form_valid(form)

class VistaListaDonadores(ListView):
    model = Donativo
    template_name = 'donar/lista_donadores.html'