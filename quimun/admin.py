from django.contrib import admin
from quimun.models import Cliente, Empresa, Arriendo

# Register your models here.
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display =  ['id', 'rut']

@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display =  ['id']

@admin.register(Arriendo)
class ArriendoAdmin(admin.ModelAdmin):
    list_display =  ['id_cliente', 'id_empresa']


