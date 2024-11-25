from django.urls import path
from . import views

urlpatterns = [
    path('jugar/', views.registro_cliente_y_ruleta, name='registro_cliente_y_ruleta'),
]