from django.contrib import admin

from apps.fight.models import Fight
from .models import Atleta
# Register your models here.




@admin.register(Atleta)
class AtletaAdmin(admin.ModelAdmin):
    list_display = ['nome',
'idade',
'peso',
'cidade',
'faixa']
    list_display_links=['nome',
'idade',
'peso',
'cidade',
'faixa']