from django.views.generic import ListView, DetailView, FormView
from django.views import View
from django.urls import reverse_lazy, reverse
from .models import Metodo
from .filtros import aplicar_filtro, aplicar_filtros_dinamicos
from .forms import FormularioComentario

# Mixins
from django.views.generic.detail import SingleObjectMixin

# /
class VistaListaMetodos(ListView):
    model = Metodo
    template_name = 'metodos/inicio.html'

class ComentarioGet(DetailView):
    model = Metodo
    template_name = 'metodos/detalle_metodo.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = FormularioComentario()
        return context

class ComentarioPost(SingleObjectMixin, FormView):
    model = Metodo
    form_class = FormularioComentario
    template_name = 'metodos/detalle_metodo.html'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post( request, *args, **kwargs )

    def form_valid(self, form):
        comentario = form.save(commit = False)
        comentario.metodo = self.object
        comentario.autor = self.request.user
        comentario.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        metodo = self.get_object()
        return reverse( 'detalle_metodo', kwargs = {'pk': metodo.pk} )

# /<int:pk>
class VistaDetalleMetodo(DetailView):
    def get(self, request, *args, **kwargs):
        view = ComentarioGet.as_view()
        return view( request, *args, **kwargs )

    def post(self, request, *args, **kwargs):
        view = ComentarioPost.as_view()
        return view( request, *args, **kwargs )

# /<str:filtro>
class VistaFiltroMetodos(ListView):
    model = Metodo
    template_name = 'metodos/inicio.html'

    def get_queryset(self):
        queryset = Metodo.objects.all()
        filtro = self.kwargs['filtro']
        queryset = aplicar_filtro( queryset = queryset, filtro = filtro )
        return queryset

# /filtro-dinamico/<str:variable>/<str:filtro>/
class VistaFiltrosDinamicos(ListView):
    model = Metodo
    template_name = 'metodos/inicio.html'
    
    def get_queryset(self):
        queryset = Metodo.objects.all()

        # Obtener slugs
        variable = self.kwargs['variable']
        filtro = self.kwargs['filtro']
        queryset = aplicar_filtros_dinamicos( 
            queryset = queryset,
            variable = variable,
            filtro = filtro)
        
        return queryset
