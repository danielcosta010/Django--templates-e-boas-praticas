from django.contrib import admin
from galeria.models import Fotografia

class ListandoFotografia(admin.ModelAdmin):
  list_display = ('id', 'nome', 'legenda')

admin.site.register(Fotografia, ListandoFotografia)