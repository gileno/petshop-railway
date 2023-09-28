import random
import datetime as dt
import django
import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'ultima.settings'

django.setup()

from base.models import Reserva

nomes = ["nome 1", "nome 2", "nome 3"]

for i in range(10):
    reserva = Reserva()
    reserva.nome = random.choice(nomes)
    reserva.telefone = str(random.randint(0, 9)) * 11
    reserva.data_reserva = dt.date.today() + dt.timedelta(days=random.randint(1,  5))
    reserva.observacoes = "gerado por script"
    reserva.save()
