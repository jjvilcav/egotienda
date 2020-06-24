from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from .models import Categoria, Subcategoria, Producto

class VistasView(TemplateView):
    template_name = "productos/index.html"
    
    def get_context_data(self, **kwargs):
        kwargs['categoria'] = Categoria.objects.all()
        return kwargs

    def get_context_data(self, **kwargs):
        kwargs['subcategoria'] = Subcategoria.objects.all()
        return kwargs

    def get_context_data(self, **kwargs):
        kwargs['productos'] = Producto.objects.all()
        return kwargs

class DetalladoView(TemplateView):
    template_name = "productos/detallado.html"

    def get_context_data(self, **kwargs):
        producto = kwargs.get('slug')
        kwargs['productos'] = Producto.objects.get(slug=producto)
        return kwargs