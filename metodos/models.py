from django.db import models
from django.conf import settings
from django.urls import reverse

# Create your models here.
class Metodo(models.Model):
    titulo = models.CharField( max_length = 255 )
    descripcion = models.CharField( max_length = 255)
    elemento = models.CharField( max_length = 255, blank = True, null = True )
    requisitos = models.TextField()
    obtencion = models.TextField()
    imagen = models.ImageField( upload_to = 'items/', blank = True, null = True )

    # Campos para filtrar
    tipo_item = models.CharField(
        max_length = 255, 
        choices =[
            ("ataque", "Ataque"), 
            ("defensa", "Defensa"), 
            ("forjable", "Forjable")
        ],
        default = "ataque"
    )

    tipo_arma = models.CharField(
        max_length = 255,
        choices = [
            ("ninguno", "Ninguno"),
            ("espada_larga", "Espada Larga"),
            ("espada_corta", "Espada Corta"),
            ("baston", "Baston")
        ],
        default = "espada_larga"
    )

    juego = models.CharField(
        max_length = 255,
        choices = [
            ("golden_sun", "Golden Sun I"),
            ("golden_sun_2", "Golden sun II")
        ],
        default = "golden_sun" 
    )

    def __str__(self):
        return self.titulo
    
    def get_absolute_url(self):
        return reverse( "detalle_metodo", kwargs={"pk": self.pk} )

class Comentario(models.Model):
    metodo = models.ForeignKey( Metodo, on_delete = models.CASCADE )
    comentario = models.CharField( max_length = 255 )
    autor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE
    )

    def __str__(self):
        return self.comentario
    
    def get_absolute_url(self):
        return reverse("inicio")