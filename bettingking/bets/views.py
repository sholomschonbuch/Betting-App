from django.http import HttpResponse
from django.shortcuts import loader
from .models import Bets

# Create your views here.    

def bets(request):
    allbets = Bets.objects.all().values()
    template = loader.get_template('all_bets.html')
    context = {
        'allbets': allbets,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    bet = Bets.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'bet': bet,
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def testing(request):
    template = loader.get_template('template.html')
    context = {
        'fruits': ['Apple', 'Pear', 'Cherry']
    }
    return HttpResponse(template.render(context, request))