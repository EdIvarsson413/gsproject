from django.contrib import admin
from .models import Metodo, Comentario

class ComentarioEnLinea(admin.TabularInline):
    model = Comentario
    extra = 0

class MetodoAdmin(admin.ModelAdmin):
    inlines = [ ComentarioEnLinea ]

# Register your models here.
admin.site.register(Metodo, MetodoAdmin)
admin.site.register(Comentario)