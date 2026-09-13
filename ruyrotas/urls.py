from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('cad-linhas/', views.cad_linhas, name='cad_linhas'),
    path('perfil/', views.perfil_view, name='perfil'),
]

