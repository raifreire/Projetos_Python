from django.contrib import admin
from galeria.models import Fotografia

#Configurando  Django Admin
class ListandoFotografias(admin.ModelAdmin):
    list_display = ("id", "nome", "legenda")# metodo list_display usado para definir o que sera exibido no painel do django admin web quando entrarmos no banco de dados
    list_display_links = ("id", "nome")

admin.site.register(Fotografia, ListandoFotografias)#chamamos o metodo -> admin.site.register e passamos nosso Model e a função que contem as configurações de exibição