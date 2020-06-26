from django import forms
from .models import Categoria, Subcategoria

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ('titulo',)

class SubcategoriaForm(forms.ModelForm):
    class Meta:
        model = Subcategoria
        fields = ('categoria','titulo',)