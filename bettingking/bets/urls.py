from django.urls import path

from . import views

urlpatterns = [
    path('bets/', views.bets, name='bets'),
    path('bets/details/<int:id>', views.details, name='details'),
]
