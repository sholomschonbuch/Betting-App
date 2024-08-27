from django.urls import path

from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('bets/', views.bets, name='bets'),
    path('bets/details/<int:id>', views.details, name='details'),
    path('testing/', views.testing, name='testing')
]
