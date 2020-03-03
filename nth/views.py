from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import *
import urllib
import urllib.request
from django.conf import settings
import json
from django.db.utils import IntegrityError
from django.contrib import messages
from django.http import Http404

levels = {
    1 : 'level1',
    2 : 'level2',
    3 : 'level3',
    4 : 'level4',
    5 : 'level5',
}

class Home(View):
    template_name = 'nth/home.html'
    def get(self, request):
        return render(request, self.template_name, {'leaderboard':Player.objects.all().order_by('-level', 'last_time')[1:11]})
    def post(self, request):
        try:
            user = User()
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.username = request.POST['username']
            user.set_password(request.POST['password'])
            user.email = request.POST['email']

            recaptcha_response = request.POST.get('g-recaptcha-response')
            url = 'https://www.google.com/recaptcha/api/siteverify'
            values = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
            data = urllib.parse.urlencode(values).encode()
            req =  urllib.request.Request(url, data=data)
            response = urllib.request.urlopen(req)
            result = json.loads(response.read().decode())

            if not result['success']:
                messages.error(request, 'Invalid reCAPTCHA. Please try again.')
                return render(request, self.template_name, {'leaderboard':Player.objects.all().order_by('-level', 'last_time')[1:11]})
            user.save()
            player = Player()
            player.user = user
            player.mobile_number = request.POST['mobile_number']
            player.college = request.POST['college']
            player.save()
            messages.error(request, 'Successfully Registered!')
        except IntegrityError:
            messages.error(request, 'Username Already Exists!')
        return render(request, self.template_name, {'leaderboard':Player.objects.all().order_by('-level', 'last_time')[1:11]})

class Login(View):
    template_name = 'nth/login.html'
    def get(self, request):
        if request.user.is_authenticated:
           player = Player.objects.get(user = request.user)
           if player.user.is_staff: return redirect('/' + levels[len(levels)])
           return redirect('/' + levels[player.level])
        else: return render(request, self.template_name)
    def post(self, request):
        user = authenticate(username = request.POST['username'], password = request.POST['password'])
        if user is not None:
            login(request, user)
            player = Player.objects.get(user = request.user)
            if player.user.is_staff: return redirect('/' + levels[len(levels)])
            return redirect('/' + levels[player.level])
        else:
            messages.error(request, 'Invalid Credentials!')
            return render(request, self.template_name)

def Logout(request):
    logout(request)
    return redirect('/')

def level1(request):
    if not request.user.is_authenticated: raise Http404("Page Does Not Exist!")
        # messages.error(request, "Please Login First!")
        # return redirect("/loginHunt/")

    player = Player.objects.get(user = request.user)
    rank = getRank(player)

    return render(request, 'nth/level1.html', {'player' : player, 'leaderboard':Player.objects.all().order_by('-level', 'last_time')[1:11], 'rank' : rank})

def level2(request):
    if not request.user.is_authenticated: raise Http404("Page Does Not Exist!")

    player = Player.objects.get(user = request.user)
    rank = getRank(player)

    if player.level == 1:
        player.level = 2
        player.save()
    return render(request, 'nth/level2.html', {'player' : player, 'leaderboard':Player.objects.all().order_by('-level', 'last_time')[1:11], 'rank' : getRank(player)})

def level3(request):
    if not request.user.is_authenticated: raise Http404("Page Does Not Exist!")

    player = Player.objects.get(user = request.user)
    rank = getRank(player)

    if player.level < 2: raise Http404("Page Does Not Exist!")
    else:
        if player.level == 2:
            player.level = 3
            player.save()
        return render(request, 'nth/level3.html', {'player' : player, 'leaderboard':Player.objects.all().order_by('-level', 'last_time')[1:11], 'rank' : getRank(player)})

def level4(request):
    if not request.user.is_authenticated: raise Http404("Page Does Not Exist!")

    player = Player.objects.get(user = request.user)
    rank = getRank(player)

    if player.level < 3: raise Http404("Page Does Not Exist!")
    else:
        if player.level == 3:
            player.level = 4
            player.save()
        return render(request, 'nth/level4.html', {'player' : player, 'leaderboard':Player.objects.all().order_by('-level', 'last_time')[:10], 'rank' : getRank(player)})

def level5(request):
    if not request.user.is_authenticated: raise Http404("Page Does Not Exist!")

    player = Player.objects.get(user = request.user)
    rank = getRank(player)

    if player.level < 4: raise Http404("Page Does Not Exist!")

    else:
        if player.level == 4:
            player.level = 5
            player.save()
        return render(request, 'nth/level5.html', {'player' : player, 'leaderboard':Player.objects.all().order_by('-level', 'last_time')[1:11], 'rank' : getRank(player)})

def getRank(player):
    rank = 0
    for p in Player.objects.all().order_by('-level', 'last_time'):
        if p == player: break
        rank = rank + 1
    return rank

def logs(request):
    template_name = 'nth/logs.html'
    return render(request, template_name, {'players':Player.objects.all(), 'count':len(User.objects.filter(is_staff=False))})
