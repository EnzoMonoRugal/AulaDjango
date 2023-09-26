from django.urls import path
from . import views
from .forms import UsuarioForm
from django.shortcuts import redirect


urlpatterns = [
    path('', views.index, name='index' ),
    path('accesses', views.access_view),
    path('pages', views.page_view),
    path('base/', views.index, name='base_view'),
    path('math/', views.match, name='math_view'),
    path('forms/',views.cadastrar_usuario, name='forms_view'),
    
]

