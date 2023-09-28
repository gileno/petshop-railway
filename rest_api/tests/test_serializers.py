import pytest
import datetime as dt

from rest_api.serializers import ReservaSerializer


@pytest.mark.django_db
def test_serializer_data_invalida():
    dados = {
        "nome_pet": "teste",
        "observacoes": "teste",
        "telefone": "1111111111",
        "data_reserva": dt.date.today() - dt.timedelta(days=1),
    }
    serializer = ReservaSerializer(data=dados)
    assert serializer.is_valid() == False
    assert 'data_reserva' in serializer.errors
    assert 'A reserva não pode ser feita no passado!' in serializer.errors['data_reserva']
