from django.contrib import admin, messages

from base.models import Contato, Reserva, Petshop


@admin.action(description='Marcar como lido')
def marcar_como_lido(modeladmin, request, queryset):
    queryset.update(lido=True)
    modeladmin.message_user(request, 'Marcado como lido!', messages.SUCCESS)

@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email', 'lido', 'data']
    search_fields = ['nome', 'email']
    list_filter = ['data']
    actions = [marcar_como_lido]


@admin.register(Petshop)
class PetshopAdmin(admin.ModelAdmin):
    list_display = ['nome', 'telefone']
    search_fields = ['nome', 'telefone', 'endereco']


@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):

    list_display = ['nome_pet', 'telefone', 'data_reserva']
    search_fields = ['nome_pet', 'telefone']
