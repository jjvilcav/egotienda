from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from .models import Usuario

class UsuarioView(TemplateView):
    template_name = "usuarios/index.html"
    
    def get_context_data(self, **kwargs):
        kwargs['usuarios'] = Usuario.objects.all()
        return kwargs