import logging
from django.shortcuts import render
from random import randint, choice
from .models import Coin, Cube, Number
from .forms import GameForm

logger = logging.getLogger(__name__)


def games(request):
    if request.method == 'POST':
        resultat = []
        form = GameForm(request.POST)
        if form.is_valid():
            game = form.cleaned_data['game']
            count_game = form.cleaned_data['count_game']
            logger.info(f'Представление game {game = }, {count_game = }')
            bd_games = {'coin': Coin, 'cube': Cube, 'number': Number}

            for _ in range(count_game):
                games = {
                    'coin': choice(['Орел', 'Решка']),
                    'cube': randint(1, 6),
                    'number': randint(1, 100)
                }
                result_game = games[game]
                res_game = bd_games[game](name=game, result=result_game)
                res_game.save()
                resultat.append(result_game)
            context = {
                'resultat': enumerate(resultat, 1),
                'name_game': game,
                'title': f'Game: {game}'
            }
            return render(request, 'games/game.html', context)

    else:
        form = GameForm()
    return render(request, "games/index.html", {'form': form, 'title': 'Игра на выбор!'})
