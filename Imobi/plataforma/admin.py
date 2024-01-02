from django.contrib import admin
from .models import DiasVisita, Horario, Imoveis, Cidade, Imagem, Visitas

@admin.register(Imoveis)
class ImoveiAdmin(admin.ModelAdmin):
    list_display = ('rua', 'numero', 'valor', 'quartos', 'tamanho', 'cidade', 'tipo')
    list_editable = ('valor', 'tipo')
    list_filter = ('cidade', 'tipo')

admin.site.register(DiasVisita)
admin.site.register(Horario)
admin.site.register(Imagem)
admin.site.register(Cidade)
admin.site.register(Visitas)