from django.urls import path
from . import views
from .forms import UsuarioForm


urlpatterns = [
    path('topics', views.topic_view),
    path('accesses', views.access_view),
    path('pages', views.page_view),
    path('base', views.index),
    path('math/', views.match),
    path('forms/',views.cadastrar_usuario),
]

