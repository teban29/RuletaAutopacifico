from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Cliente, Premio, Ruleta, Ganador, Configuracion
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import ClienteForm, PremioForm, GanadorForm, ConfiguracionForm
import random

class AdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        # Solo permitir usuarios con is_staff o is_superuser
        return self.request.user.is_staff or self.request.user.is_superuser

@login_required
@user_passes_test(lambda u: u.is_staff or u.is_superuser)
def admin_main_page(request):
    return render(request, 'ruleta/admin_main_page.html')

@login_required
@user_passes_test(lambda u: u.is_staff or u.is_superuser)
def premio_toggle(request, pk):
    premio = get_object_or_404(Premio, pk=pk)
    premio.activo = not premio.activo  # Cambiar el estado de activo/inactivo
    premio.save()
    return redirect('premio_list')

def registro_cliente_y_ruleta(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save()

            # Obtener todos los premios
            premios = Premio.objects.all()

            # Determinar el premio ganado en función de la probabilidad
            premio_ganado = determinar_premio(premios)

            # Crear el registro de la ruleta
            ruleta = Ruleta(cliente=cliente, premio=premio_ganado)
            ruleta.save()

            # Si ganó un premio, registrarlo en Ganador
            if premio_ganado:
                Ganador.objects.create(cliente=cliente, premio=premio_ganado)

            return redirect('resultado', cliente_id=cliente.id)

    else:
        form = ClienteForm()

    return render(request, 'ruleta/registro_y_juego.html', {'form': form})

import random

def determinar_premio(premios):
    try:
        config = Configuracion.objects.latest('id')
        probabilidad_no_ganar = config.probabilidad_no_ganar
    except Configuracion.DoesNotExist:
        probabilidad_no_ganar = 30  # Usa un valor por defecto si no se ha configurado

    total_probabilidad = probabilidad_no_ganar + sum(premio.probabilidad for premio in premios)
    seleccion = random.uniform(0, total_probabilidad)
    acumulador = 0
    acumulador += probabilidad_no_ganar
    if seleccion <= acumulador:
        return None  # No gana ningún premio

    for premio in premios:
        acumulador += premio.probabilidad
        if seleccion <= acumulador:
            return premio

    return None
@login_required
@user_passes_test(lambda u: u.is_staff or u.is_superuser)
def actualizar_probabilidad(request):
    if request.method == 'POST':
        nueva_probabilidad = request.POST.get('probabilidad_no_ganar')
        if nueva_probabilidad:
            Configuracion.objects.update_or_create(
                id=1,  # Asumiendo que siempre trabajamos con un registro
                defaults={'probabilidad_no_ganar': float(nueva_probabilidad)}
            )
        return redirect('premio_list')

    probabilidad_actual = Configuracion.objects.first().probabilidad_no_ganar if Configuracion.objects.exists() else 30
    return render(request, 'ruleta/premio_list.html', {'probabilidad_actual': probabilidad_actual})


def resultado(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    ruleta = Ruleta.objects.filter(cliente=cliente).latest('fecha_tiro')

    contexto = {
        'cliente': cliente,
        'premio_ganado': ruleta.premio
    }
    return render(request, 'ruleta/resultado.html', contexto)


# CRUD PARA PREMIOS
class PremioListView(LoginRequiredMixin, AdminRequiredMixin, ListView):
    model = Premio
    template_name = 'ruleta/premios_list.html'
    context_object_name = 'premios'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Obtener la última configuración de probabilidad y pasarla al contexto
        context['probabilidad_actual'] = Configuracion.objects.first().probabilidad_no_ganar if Configuracion.objects.exists() else 30
        return context

class PremioCreateView(LoginRequiredMixin, AdminRequiredMixin, CreateView):
    model = Premio
    form_class = PremioForm
    template_name = 'ruleta/premio_form.html'
    success_url = reverse_lazy('premio_list')

class PremioUpdateView(LoginRequiredMixin, AdminRequiredMixin, UpdateView):
    model = Premio
    form_class = PremioForm
    template_name = 'ruleta/premio_form.html'
    success_url = reverse_lazy('premio_list')

class PremioDeleteView(LoginRequiredMixin, AdminRequiredMixin, DeleteView):
    model = Premio
    template_name = 'ruleta/premio_confirm_delete.html'
    success_url = reverse_lazy('premio_list')


# CRUD PARA CLIENTES
class ClienteListView(LoginRequiredMixin, AdminRequiredMixin, ListView):
    model = Cliente
    template_name = 'ruleta/clientes_list.html'
    context_object_name = 'clientes'

class ClienteCreateView(LoginRequiredMixin, AdminRequiredMixin, CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'ruleta/cliente_form.html'
    success_url = reverse_lazy('cliente_list')

class ClienteUpdateView(LoginRequiredMixin, AdminRequiredMixin, UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'ruleta/cliente_form.html'
    success_url = reverse_lazy('cliente_list')

class ClienteDeleteView(LoginRequiredMixin, AdminRequiredMixin, DeleteView):
    model = Cliente
    template_name = 'ruleta/cliente_confirm_delete.html'
    success_url = reverse_lazy('cliente_list')


# CRUD PARA GANADORES
class GanadorListView(LoginRequiredMixin, AdminRequiredMixin, ListView):
    model = Ganador
    template_name = 'ruleta/ganadores_list.html'
    context_object_name = 'ganadores'

class GanadorCreateView(LoginRequiredMixin, AdminRequiredMixin, CreateView):
    model = Ganador
    form_class = GanadorForm
    template_name = 'ruleta/ganador_form.html'
    success_url = reverse_lazy('ganador_list')

class GanadorUpdateView(LoginRequiredMixin, AdminRequiredMixin, UpdateView):
    model = Ganador
    form_class = GanadorForm
    template_name = 'ruleta/ganador_form.html'
    success_url = reverse_lazy('ganador_list')

class GanadorDeleteView(LoginRequiredMixin, AdminRequiredMixin, DeleteView):
    model = Ganador
    template_name = 'ruleta/ganador_confirm_delete.html'
    success_url = reverse_lazy('ganador_list')