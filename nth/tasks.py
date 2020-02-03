from __future__ import absolute_import, unicode_literals
from celery import task
from .models import Player

leaderboard = Player.objects.all()

@task()
def generate_leaderboard():
    leaderboard = Player.objects.all().order_by('-level', 'last_time')
    print(leaderboard)