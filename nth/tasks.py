from __future__ import absolute_import, unicode_literals
from celery import task
from .models import *

@task()
def generate_leaderboard():
    leaderboard = Player.objects.all().order_by('-level', 'last_time')
    Leaderboard.objects.all().delete()
    for player in leaderboard:
        Leaderboard.objects.create(player=player)
    print(leaderboard)