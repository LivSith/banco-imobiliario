import random
from django.shortcuts import render
from .models import Board, Property, Player


def game(request):
    board = Board.objects.all()
    properties = Property.objects.all()
    players = Player.objects.all()
    dado = __get_d6__

    #for prayer  in players:
        #d6 = choices()

    context = {
        'board' : board,
        'properties' : properties,
        'player' : players,
        'dice' : dado
    }

    return render(request, 'index.html', context)

# Nosso dado D6
def __get_d6__():
    min_value = 1
    max_value = 6

    return (random.randint(min_value, max_value))