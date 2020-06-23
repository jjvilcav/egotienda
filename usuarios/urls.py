from django.conf.urls import url
from django.urls import path
from .views import UsuarioView

urlpatterns = [
    path('',UsuarioView.as_view(),name='index'),
]