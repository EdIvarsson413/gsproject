from .models import UsuarioPers
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class FormCreacionUsuario(UserCreationForm):
    class Meta(UserCreationForm):
        model = UsuarioPers
        fields = ( 'username', 'email', 'edad' )

class FormCambiarUsuario(UserChangeForm):
    class Meta:
        model = UsuarioPers
        fields = ( 'username', 'email', 'edad' )