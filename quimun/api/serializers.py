from rest_framework.serializers import ModelSerializer
from quimun.models import Cliente, Empresa, Arriendo

class ClienteSerializer(ModelSerializer):
    class Meta: 
        model = Cliente
        fields = ['id', 'rut', 'name']

class EmpresaSerializer(ModelSerializer):
    class Meta: 
        model = Empresa
        fields = ['id', 'name']

class ArriendoSerializer(ModelSerializer):
    class Meta: 
        model = Arriendo
        fields = ['id_cliente', 'id_empresa', 'costo_diario', 'dias']                