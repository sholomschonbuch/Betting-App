from django.db import models

# Create your models here.
class Bets(models.Model):
    name = models.CharField(max_length=200)
    bet_amount = models.IntegerField()
    odds = models.FloatField()
    payout = models.FloatField()
    win = models.BooleanField(default=False)
    date = models.DateTimeField()