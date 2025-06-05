from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('compromisso', views.mostrar_compromisso, name='motrar_compromisso'),
    path('marcar', views.marcar, name='marcar')
]
