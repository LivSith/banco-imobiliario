import random
from django.shortcuts import render
from .models import Board, Property, Player


def game(request):
    board = Board.objects.all()
    properties = Property.objects.all()
    players = Player.objects.all()
    dice = random.randint(1, 6)

    print ('quantidade de propriedades', len(properties))
    result = 0
    for player in players:
        result += dice
        if result < len(properties):
            continue
        else:
            result = int(len(properties)) - result
            player.purchase_balance + 100
            if player.personality == 'I':
                print ('comprei', properties[result])
            print ('player: ', player.name, 'saldo: ', player.purchase_balance)

    context = {
        'board' : board,
        'properties' : properties,
        'player' : players,
        'dice' : dice
    }

    return render(request, 'index.html', context)