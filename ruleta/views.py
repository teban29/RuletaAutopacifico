from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Cliente, Premio, Ruleta, Ganador
from .forms import ClienteForm
import random

def registro_cliente_y_ruleta(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save()

            # Realizar el tiro en la ruleta
            premios = Premio.objects.all()
            premio_ganado = None

            # Determinar si el cliente gana un premio según la probabilidad de cada uno
            for premio in premios:
                if random.random() < premio.probabilidad:
                    premio_ganado = premio
                    break

            # Crear el registro de la ruleta
            ruleta = Ruleta(cliente=cliente, premio=premio_ganado)
            ruleta.save()

            # Si ganó un premio, registrarlo en Ganador
            if premio_ganado:
                Ganador.objects.create(cliente=cliente, premio=premio_ganado)

            return redirect('resultado', cliente_id=cliente.id)  # Redirige a una vista de resultados

    else:
        form = ClienteForm()

    return render(request, 'ruleta/registro_y_juego.html', {'form': form})
