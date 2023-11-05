from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import FormCreacionUsuario, FormCambiarUsuario
from .models import UsuarioPers

# Register your models here.
class UsuarioAdmin(UserAdmin):
    add_form = FormCreacionUsuario
    form = FormCambiarUsuario
    model = UsuarioPers
    list_display = [
        'email',
        'username',
        'edad',
        'is_staff'
    ]
    fieldsets = UserAdmin.fieldsets + ((None, { 'fields': ('edad',) }),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {'fields': ('edad'),}),)

# Mostrar en el panel de Admin
admin.site.register( UsuarioPers, UsuarioAdmin );