
from django.contrib import admin
from .models import Nacionalidad, Cliente, TipoMoto, Moto, Alquiler

class NacionalidadAdmin(admin.ModelAdmin):
    list_display = ('nacionalidad_id', 'nacionalidad')

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('ndi', 'nombres', 'apellido_paterno', 'apellido_materno', 'telefono', 'direccion', 'nacionalidad')
    search_fields = ('ndi', 'nombres', 'apellido_paterno', 'apellido_materno')

class TipoMotoAdmin(admin.ModelAdmin):
    list_display = ('tipo_id', 'tipo')

class MotoAdmin(admin.ModelAdmin):
    list_display = ('moto_id', 'placa', 'color', 'tipo', 'modelo', 'tarifa', 'estado')
    list_filter = ('estado', 'tipo')
    search_fields = ('placa', 'modelo')

class AlquilerAdmin(admin.ModelAdmin):
    list_display = ('alquiler_id', 'fecha', 'hora_inicio', 'hora_fin', 'cantidad_horas', 'estado', 'monto', 'cliente', 'moto')
    list_filter = ('estado', 'fecha')
    search_fields = ('cliente__nombres', 'cliente__apellido_paterno', 'cliente__apellido_materno', 'moto__placa')

admin.site.register(Nacionalidad, NacionalidadAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(TipoMoto, TipoMotoAdmin)
admin.site.register(Moto, MotoAdmin)
admin.site.register(Alquiler, AlquilerAdmin)
