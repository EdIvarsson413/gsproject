from django.db import models
from django.conf import settings
from django.urls import reverse
from django.core.validators import MinValueValidator

# Create your models here.
class Donativo(models.Model):
    cantidad = models.IntegerField( 
        validators = [MinValueValidator(0)],
        help_text = "Ingresa la cantidad que deseas donar"
    )
    donador = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE,
    )

    def __str__(self):
        return self.donador.username
    

    def get_absolute_url(self):
        return reverse( "inicio" )
    