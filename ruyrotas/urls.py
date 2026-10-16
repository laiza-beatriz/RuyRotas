from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("linhas/", views.linhas, name="linhas"),
    path('cad-linhas/', views.cad_linhas, name='cad_linhas'),
    path('perfil/', views.perfil, name='perfil'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path("perfil/editar/", views.editar_perfil, name="editar_perfil"),
]