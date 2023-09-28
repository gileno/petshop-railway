import datetime as dt
from rest_framework import serializers

from base.models import Reserva, Petshop


class ReservaPetshopSerializer(serializers.ModelSerializer):

    class Meta:
        model = Petshop
        fields = [
            'id',
            'nome',
            'telefone',
            'endereco',
        ]


class PetShopPrimaryKeyRelatedField(serializers.PrimaryKeyRelatedField):

    def use_pk_only_optimization(self):
        return False

    def to_representation(self, value):
        return ReservaPetshopSerializer(instance=value).data


class ReservaSerializer(serializers.ModelSerializer):

    petshop_info = serializers.SerializerMethodField()

    def get_petshop_info(self, obj):
        serializer = ReservaPetshopSerializer(instance=obj.petshop)
        return serializer.data

    def validate_data_reserva(self, value):
        if value < dt.date.today():
            raise serializers.ValidationError('A reserva não pode ser feita no passado!')
        return value
    
    class Meta:
        model = Reserva
        fields = [
            'id',
            'nome_pet',
            'telefone',
            'data_reserva',
            'observacoes',
            'petshop',
            'petshop_info'
        ]


class PetshopSerializer(serializers.ModelSerializer):

    quantidade_reservas = serializers.SerializerMethodField()
    reservas = serializers.HyperlinkedRelatedField(
        view_name='api:reserva-detail',
        read_only=True,
        many=True,
    )

    def get_quantidade_reservas(self, obj):
        return Reserva.objects.filter(petshop=obj).count()
    
    class Meta:
        model = Petshop
        fields = [
            'id',
            'nome',
            'telefone',
            'endereco',
            'quantidade_reservas',
            'reservas',
        ]
