from django.contrib import admin

# Register your models here.
from .models import Categoria, Subcategoria, Producto
admin.site.register(Categoria)
admin.site.register(Subcategoria)
admin.site.register(Producto)