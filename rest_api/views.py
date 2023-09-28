import json
import datetime as dt

from django.http import HttpResponse

from rest_framework.permissions import (
    IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny, BasePermission
)
from rest_framework.viewsets import ModelViewSet

from base.models import Reserva, Petshop

from rest_api.serializers import ReservaSerializer, PetshopSerializer

def inicio(request):
    reservas = Reserva.objects.all()
    dados = []
    for reserva in reservas:
        dados.append({
            'id': reserva.id,
            'nome_pet': reserva.nome_pet,
            'telefone': reserva.telefone,
            'data_reserva': reserva.data_reserva.strftime('%d/%m/%Y'), # 03/08/2023
            'observacoes': reserva.observacoes,
        })
    return HttpResponse(json.dumps(dados))

'''
/api/reservas - GET (listar) list
/api/reservas - POST (criar) create
/api/reservas/1 - GET (detalhar) retrieve
/api/reservas/1 - DELETE (apagar) destroy
/api/reservas/1 - PUT (atualizar totalmente) update
/api/reservas/1 - PATCH (atualizar parcialmente) partial_update
'''

class UltimaPermission(BasePermission):

    def has_permission(self, request, view):
        # a lógica específica do meu negócio
        return bool(request.user and request.user.is_authenticated)


class ReservaViewSet(ModelViewSet):

    # queryset = Reserva.objects.all()
    filterset_fields = {
        'nome_pet': ['icontains'],
        'data_reserva': ['gte', 'lte'],
        'petshop': ['exact'],
    }
    serializer_class = ReservaSerializer
    
    def get_queryset(self):
        return Reserva.objects.all()

    def get_permissions(self):
        if self.action == 'create':
            return [AllowAny()]
        return [IsAuthenticated()]


class PetshopViewSet(ModelViewSet):

    queryset = Petshop.objects.all()
    serializer_class = PetshopSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
