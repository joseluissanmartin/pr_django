from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework import status
from quimun.models import Cliente, Empresa, Arriendo
from quimun.api.serializers import ClienteSerializer, EmpresaSerializer, ArriendoSerializer

class ClienteApiViewSet(ModelViewSet):
    serializer_class = ClienteSerializer
    queryset = Cliente.objects.all()

class EmpresaApiViewSet(ModelViewSet):
    serializer_class = EmpresaSerializer
    queryset = Empresa.objects.all()

class ArriendoApiViewSet(ModelViewSet):
    serializer_class = ArriendoSerializer
    queryset = Arriendo.objects.all()   

class ClienteID(RetrieveAPIView):
    serializer_class = ClienteSerializer
    queryset = Cliente.objects.all()
    lookup_field = 'id'

    def retrieve(self, request, *args, **kwargs):
        cliente_id = kwargs.get('id')
        try:
            cliente = Cliente.objects.get(id=cliente_id)
            serializer = self.get_serializer(cliente)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Cliente.DoesNotExist:
            return Response({"detail": "Cliente no encontrado."}, status=status.HTTP_404_NOT_FOUND)

class ClientesPorApellido(ListAPIView):
    serializer_class = ClienteSerializer
    def get_queryset(self):
        queryset = Cliente.objects.all()
        queryset = sorted(queryset, key=lambda x: x.name.split(' ')[-1])
        return queryset
    
# class ArriendoPorGasto(ListAPIView):
#     serializer_class = ArriendoSerializer
#     def get_queryset(self):
#         # Ordenar los arriendos por costo_diario de mayor a menor
#         queryset = Arriendo.objects.all()
#         queryset = sorted(queryset, key=lambda x: x.costo_diario, reverse=True)
#         return queryset       