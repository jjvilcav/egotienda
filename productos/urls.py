from django.conf.urls import url
from django.urls import path
from .views import VistasView

urlpatterns = [
    path('',VistasView.as_view(),name='index'),
]