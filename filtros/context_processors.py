from .models import Filtro
from contacto.models import Metodo

def links(request):
    links = Filtro.objects.all()
    return dict(links = links)