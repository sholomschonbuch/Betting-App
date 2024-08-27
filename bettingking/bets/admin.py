from django.contrib import admin
from .models import Bets

class BetAdmin(admin.ModelAdmin):
    list_display = ("name", "bet_amount")
    
admin.site.register(Bets, BetAdmin)