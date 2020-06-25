from django.conf.urls import url
from django.urls import path
from .views import VistasView, DetalladoView, NuevaCategoriaView

urlpatterns = [
    path('',VistasView.as_view(),name='index'),
    path('<slug:slug>', DetalladoView.as_view(),name='detallado'),
    path('formulario/',NuevaCategoriaView.as_view(),name='formulario'),
]

