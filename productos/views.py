from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from .models import Categoria, Subcategoria, Producto
from .forms import CategoriaForm, SubcategoriaForm

class VistasView(TemplateView):
    template_name = "productos/index.html"
    
    def get_context_data(self, **kwargs):
        kwargs['categoria'] = Categoria.objects.all()
        kwargs['subcategoria'] = Subcategoria.objects.all()
        kwargs['productos'] = Producto.objects.all()
        return kwargs

class DetalladoView(TemplateView):
    template_name = "productos/detallado.html"

    def get_context_data(self, **kwargs):
        producto = kwargs.get('slug')
        kwargs['productos'] = Producto.objects.get(slug=producto)
        return kwargs

class NuevaCategoriaView(TemplateView):
    template_name = "productos/form.html"

    def get_context_data(self, **kwargs):
        kwargs['form'] = CategoriaForm
        return kwargs
    
    def post(self,request,*args,**kwargs):
        context = self.get_context_data(**kwargs)
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
        context['form']=form
        return self.render_to_response(context)

class NuevaSubcategoriaView(TemplateView):
    template_name = "productos/sub.html"

    def get_context_data(self, **kwargs):
        kwargs['form'] = SubcategoriaForm
        return kwargs
    
    def post(self,request,*args,**kwargs):
        context = self.get_context_data(**kwargs)
        form = SubcategoriaForm(request.POST)
        if form.is_valid():
            form.save()
        context['form']=form
        return self.render_to_response(context)