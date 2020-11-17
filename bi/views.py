import random
from django.shortcuts import render
from .models import Board, Property, Player


def game(request):
    board = Board.objects.all()
    properties = Property.objects.all()
    players = Player.objects.all()
    # Cria tabuleiro
    nome_tabuleiro = 'Teste_1'
    if len(board) == 0:
        new_board = Board(name=nome_tabuleiro)
        new_board.save()
    # Cria as 20 propriedades
    elif len(board) == 1:

        for item in board:
            board_name = item
            print(board_name)
            name_properties = 0
            new_to_buy = 40
            new_to_rent = 20
            print(len(properties))
            if len(properties) < 20:
                if name_properties != 20:
                    name_properties += 1
                    new_to_buy += 20
                    new_to_rent += 10
                    new_properties = Property(name=name_properties, board=board_name, to_buy=new_to_buy, to_rent=new_to_rent)
                    new_properties.save()
                else:
                    print ('Vcjá possui ', len(properties), ' propriedades.')
    else:
        print( "vc possui mais de um tabuleiro")

    print ('quantidade de propriedades', len(properties)) #tirar depois

    #Cria os 4 jogadores
    if len(players) == 0:
        players_name = i.id
        purchase_balance = 300
        persona_impusive = 'I'
        persona_demanding = 'E'
        persona_cautious = 'C'
        persona_random = 'A'

        player_i = Player(name=players_name, personality=persona_impusive, purchase_balance=purchase_balance)
        player_i.save()
        player_d = Player(name=players_name, personality=persona_demanding, purchase_balance=purchase_balance)
        player_d.save()
        player_c = Player(name=players_name, personality=persona_cautious, purchase_balance=purchase_balance)
        player_c.save()
        player_r = Player(name=players_name, personality=persona_random, purchase_balance=purchase_balance)
        player_r.save()

    context = {
        'board' : board,
        'properties' : properties,
        'player' : players,
    }
    
    context['data'] = {}
    game_round = 0
    if game_round < 300:
        game_round += 1

        
        for i in players:

            context['data'].setdefault(i.id, {})['jogadores'] = i.personality
            context['data'][i.id]['saldo'] = i.purchase_balance
            context['data'][i.id]['d6'] = random.randint(1, 6)

    

    return render(request, 'index.html', context)