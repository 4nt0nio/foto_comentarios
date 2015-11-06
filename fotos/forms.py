from django.forms import ModelForm
from django import forms
from .models import Foto, Cometario

class FotoForm(forms.ModelForm):
    class Meta:
        model = Foto
        fields = ('titulo','foto','favorito','categoria','descripcion')


class CometarioForm(forms.ModelForm):
    class Meta:
        model = Cometario
        fields = ('cometario',)
    