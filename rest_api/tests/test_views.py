import pytest
import datetime as dt

from model_bakery import baker

from rest_framework.test import APIClient


@pytest.fixture
def reserva_dados():
    return {
        "nome_pet": "teste",
        "telefone": "11111111111",
        "data_reserva": dt.date.today().strftime("%d/%m/%Y"),
        "observacoes": "teste",
    }


@pytest.mark.django_db
def test_reserva_listagem():
    baker.make('base.Reserva', _quantity=20)
    cliente = APIClient()
    resposta = cliente.get("/api/reservas")
    assert resposta.status_code == 401
    usuario = baker.make('auth.User')
    cliente.force_authenticate(usuario)
    resposta = cliente.get("/api/reservas")
    assert resposta.status_code == 200
    resultados = resposta.data["results"]
    assert len(resultados) == 10


@pytest.mark.django_db
def test_criar_reserva(reserva_dados):
    cliente = APIClient()
    resposta = cliente.post("/api/reservas", reserva_dados)
    assert resposta.status_code == 201
    assert resposta.data["nome_pet"] == "teste"


@pytest.mark.django_db
def test_atualizar_reserva():
    reserva = baker.make("base.Reserva")
    cliente = APIClient()
    # Reserva.objects.filter(nome_pet="teste")
    # "select * from base_reserva where nome_pet = 'teste'"
    # Reserva.objects.raw("select nome_pet, telefone, data_reserva, observacoes, petshop_id from base_reserva where algo complexo")
    usuario = baker.make('auth.User')
    cliente.force_authenticate(usuario)
    resposta = cliente.patch(f"/api/reservas/{reserva.pk}", {"nome_pet": "novo pet"})
    assert resposta.status_code == 200
    assert resposta.data["nome_pet"] == "novo pet"
