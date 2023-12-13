from django.db import models
from django.conf import settings
from django.urls import reverse
import uuid

# Create your models here.
class Metodo(models.Model):
    id = models.UUIDField( 
        primary_key = True, 
        default = uuid.uuid4, 
        editable = False
    ) 
    titulo = models.CharField( max_length = 255 )
    descripcion = models.CharField( max_length = 255)
    elemento = models.CharField( 
        max_length = 255,
        choices = [
            ("Ninguno", "Ninguno"),
            ("Venus", "Venus"),
            ("Marte", "Marte"),
            ("Jupiter", "Jupiter"),
            ("Mercurio", "Mercurio")
        ]
    )
    requisitos = models.TextField()
    instrucciones = models.TextField()
    autor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE,
    )

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

    class Meta:
        permissions = [
            ('special_status', 'Can read all the methods')
        ]

    def __str__(self):
        return self.titulo
    
    def get_absolute_url(self):
        return reverse( "detalle_nuevo", args = [ str(self.pk) ] )