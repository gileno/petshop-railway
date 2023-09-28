import pytest
import datetime as dt

from model_bakery import baker
from base.models import Petshop, Reserva


@pytest.fixture
def petshop():
    petshop = baker.make(Petshop)
    baker.make(Reserva, petshop=petshop, _quantity=10)
    return petshop


@pytest.mark.django_db
def test_metodo_str_reserva():
    # reserva = baker.make('base.Reserva')
    reserva = baker.make(Reserva, nome_pet='teste', telefone='(11)99999.9999')
    assert str(reserva) == '[(11)99999.9999] teste'


@pytest.mark.django_db
def test_quantidade_reserva_petshop(petshop):
    # petshop = baker.make(Petshop)
    # baker.make(Reserva, petshop=petshop, _quantity=10)
    assert petshop.quantidade_reservas() == 10
