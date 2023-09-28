import pytest
import datetime as dt

from pytest_django.asserts import assertContains, assertTemplateUsed

from model_bakery import baker

from base.models import Reserva, Petshop


@pytest.mark.django_db
def test_template_usado_reserva(client):
    resposta = client.get('/reserva/')
    assert resposta.status_code == 200
    assertTemplateUsed('reserva.html')


@pytest.mark.django_db
def test_reserva_criada_sucesso(client):
    dados = {
        "nome_pet": "teste nome",
        "telefone": "11111111111",
        "data_reserva": dt.date.today().strftime("%d/%m/%Y"),
        "observacoes": "teste"
    }
    resposta = client.post('/reserva/', dados)
    assertContains(resposta, "Sua reserva foi efetuada com sucesso!")
