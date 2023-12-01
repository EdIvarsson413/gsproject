from django.db import models

# Create your models here.
class Filtro(models.Model):
    nombre = models.CharField( max_length = 255 )
    elementos_filtro = models.CharField( max_length = 255, default = "" )

    def elementos(self):
        elementos = list()
        
        for elemento in self.elementos_filtro.split(','):
            elemento_limpiar = elemento.replace(" ", "_")
            elemento_lower = elemento_limpiar.lower()

            # Verificar si dice acendente o descendente
            if elemento_lower == "ascendente":
                elementos.append({ 
                    'elemento': elemento, 
                    'variable': self.nombre.lower,
                    'elemento_slug': "titulo"
                })
            elif elemento_lower == "descendente":
                elementos.append({ 
                    'elemento': elemento, 
                    'variable': self.nombre.lower,
                    'elemento_slug': "-titulo"
                    })
            else:
                variable_limpiar = self.nombre.replace(' ', '_')
                variable_filtro = variable_limpiar.lower()
                elementos.append({ 
                    'elemento': elemento,
                    'variable': variable_filtro, 
                    'elemento_slug': elemento_lower 
                })

        return elementos

    def __str__(self):
        return self.nombre