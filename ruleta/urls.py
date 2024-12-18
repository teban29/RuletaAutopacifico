from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Hacer que la página de login sea la principal
    path('', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('actualizar-probabilidad/', views.actualizar_probabilidad, name='actualizar_probabilidad'),

    # URLs para registro de cliente y resultado
    path('registro/', views.registro_cliente, name='registro_cliente_y_ruleta'),
    path('jugar/', views.jugar_ruleta, name='jugar_ruleta'),  # Permite acceder sin cliente_id
    path('jugar/<int:cliente_id>/', views.jugar_ruleta, name='jugar_ruleta'),
    path('resultado/<int:cliente_id>/', views.resultado, name='resultado'),
    path('girar/', views.girar_ruleta, name='ruta_para_girar_ruleta'),

    
    # URLs para Clientes
    path('clientes/', views.ClienteListView.as_view(), name='cliente_list'),
    path('clientes/nuevo/', views.ClienteCreateView.as_view(), name='cliente_create'),
    path('clientes/editar/<int:pk>/', views.ClienteUpdateView.as_view(), name='cliente_update'),
    path('clientes/eliminar/<int:pk>/', views.ClienteDeleteView.as_view(), name='cliente_delete'),
    
    # URLs para Ganadores
    path('ganadores/', views.GanadorListView.as_view(), name='ganador_list'),
    path('ganadores/nuevo/', views.GanadorCreateView.as_view(), name='ganador_create'),
    path('ganadores/editar/<int:pk>/', views.GanadorUpdateView.as_view(), name='ganador_update'),
    path('ganadores/eliminar/<int:pk>/', views.GanadorDeleteView.as_view(), name='ganador_delete'),

    
    # URLs para Premios
    path('premios/', views.PremioListView.as_view(), name='premio_list'),
    path('premios/nuevo/', views.PremioCreateView.as_view(), name='premio_create'),
    path('premios/editar/<int:pk>/', views.PremioUpdateView.as_view(), name='premio_update'),
    path('premios/eliminar/<int:pk>/', views.PremioDeleteView.as_view(), name='premio_delete'),
    path('premios/toggle/<int:pk>/', views.premio_toggle, name='premio_toggle'),  # Añadir esta línea




    # URLs para cuentas
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),

    # URL para la página principal del administrador
    path('admin-main/', views.admin_main_page, name='admin_main'),
]
