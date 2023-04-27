from django.contrib import admin
from galeria.models import Fotografia

#Configurando  Django Admin
class ListandoFotografias(admin.ModelAdmin):
    list_display = ("id", "nome", "legenda")# metodo list_display usado para definir o que sera exibido no painel do django admin web quando entrarmos no banco de dados
    list_display_links = ("id", "nome")
<<<<<<< HEAD
    search_fields = ("nome",)
    list_filter = ("categoria",)
    list_per_page = 10
=======
>>>>>>> fb7e3f169cf27b1017c3af33f584ff3a51cd2f7d

admin.site.register(Fotografia, ListandoFotografias)#chamamos o metodo -> admin.site.register e passamos nosso Model e a função que contem as configurações de exibição