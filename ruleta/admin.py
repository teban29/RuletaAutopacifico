from django.contrib import admin
from .models import Cliente, Premio, Ruleta, Ganador
# Register your models here.

admin.site.register(Cliente)
admin.site.register(Premio)
admin.site.register(Ruleta)
admin.site.register(Ganador)
