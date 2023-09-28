from django.contrib import admin
from django.urls import path, include

# Importando todas as views definidas no arquvivo 'views.py' da app 'base'
from base.views import *

urlpatterns = [
    path('', inicio, name='inicio'),

    path('contato/', contato, name='contato'),
    path('reserva/', reserva, name='reserva'),

    path('login/', login_usuario, name='login_usuario'),
    path('logout/', logout_usuario, name='logout_usuario'),
    path('novo-usuario/', novo_usuario, name='novo_usuario'),

    path('api/', include('rest_api.urls', namespace='api')),

    path('api-auth/', include('rest_framework.urls')),

    path('admin/', admin.site.urls),
]
