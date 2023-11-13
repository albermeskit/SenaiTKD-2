from django.contrib import admin
from .models import Fight
# Register your models here.

@admin.register(Fight)
class FightAdmin(admin.ModelAdmin):
    list_display = ['atleta1',
'atleta2',
'data',
'faixa_atleta1',
'faixa_atleta2',
'local']
    list_display_links=['atleta1',
'atleta2',
'local']