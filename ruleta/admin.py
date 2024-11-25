from django.contrib import admin
from .models import Cliente, Premio, Ruleta, Ganador

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('numero_documento', 'nombre', 'apellidos', 'numero_celular', 'numero_factura')
    search_fields = ('numero_documento', 'nombre', 'apellidos')
    list_filter = ('numero_celular',)

@admin.register(Premio)
class PremioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'probabilidad')
    search_fields = ('nombre',)
    list_filter = ('probabilidad',)

@admin.register(Ruleta)
class RuletaAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'premio', 'fecha_tiro')
    search_fields = ('cliente__nombre', 'premio__nombre')
    list_filter = ('fecha_tiro',)

@admin.register(Ganador)
class GanadorAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'premio', 'fecha_ganador')
    search_fields = ('cliente__nombre', 'premio__nombre')
    list_filter = ('fecha_ganador',)
