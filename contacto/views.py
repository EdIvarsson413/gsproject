from django.views.generic import CreateView, ListView, DetailView
from .models import Metodo
from django.shortcuts import redirect

# Para la descarga de datos del metodo nuevo
from django.http import HttpResponse
from django.views import View

# Mixins
from django.contrib.auth.mixins import ( LoginRequiredMixin, UserPassesTestMixin )

# /nuevo-metodo/
class VistaCrearMetodo(CreateView):
    # admin o persona sin autenticarse?
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_staff:
            return redirect('inicio')
        
        return super().dispatch(request, *args, **kwargs)

    # Se requiere inicio de sesion para crear un metodo
    model = Metodo
    template_name = 'contacto/crear_metodo.html'
    fields = ( 
                "titulo", "descripcion", "elemento", 
                "requisitos", "instrucciones",
                "tipo_item", "tipo_arma", "juego"
            )

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

class VistaListaMetodosReportados(ListView):
    # usuario en la vista?
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return redirect('inicio')
        
        return super().dispatch(request, *args, **kwargs)

    model = Metodo
    template_name = 'contacto/lista_metodos.html'

class VistaDetalleMetodoNuevo(DetailView):
    # usuario en la vista?
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return redirect('inicio')
        
        return super().dispatch(request, *args, **kwargs)

    model = Metodo
    template_name = 'contacto/detalle_nuevometodo.html'

class DescargarDatos(View):
    def get(self, request, pk):
        try:
            # Obtener objeto del modelo
            objeto = Metodo.objects.get( pk = pk )

            # Nombre del archivo 
            nombre_archivo = f'datos_{objeto.titulo}.txt'

            # Crea el contenido del archivo de texto
            contenido = f"ID: {objeto.pk}\n\n"
            contenido += f"Nombre: {objeto.titulo}\n\n"
            contenido += f"Descripción:{objeto.descripcion}\n\n"
            contenido += f"Elemento: {objeto.elemento}\n\n"
            
            # Limpiar el string de requisitos (quitar dobles \n)
            contenido += "Requisitos:"
            contenido += "\n".join(objeto.requisitos.splitlines()).join("\n\n")
            contenido += "\nInstrucciones:"
            contenido += "\n".join(objeto.instrucciones.splitlines()).join("\n\n")

            contenido += f"\nOtros detalles: \n\t"
            contenido += f"Tipo de arma:\t{objeto.tipo_arma}\n\t"
            contenido += f"Tipo de item:\t{objeto.tipo_item}\n\t"
            contenido += f"Juego:\t{objeto.juego}"

            response = HttpResponse( content_type = "text/plain" )
            response["Content-Disposition"] = f'attachment; filename="{nombre_archivo}"'
            response.write( contenido )

            return response
        except Metodo.DoesNotExist:
            return HttpResponse("Objeto no encontrado", status=404)