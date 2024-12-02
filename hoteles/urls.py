from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_hoteles, name='listar_hoteles'),
]