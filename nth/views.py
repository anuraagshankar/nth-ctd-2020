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
    1:'level1', 2:'nickabadzis', 3:'sirbenjaminlockspeiser', 4:'anttirinne', 5:'bytown', 6:'patherpanchali',
    7:'vanburensupernova', 8:'deebradleybaker', 9:'andiamironman', 10:'oncology', 11:'losangeles', 12:'paracasculture',
    13:'jaahnavi', 14:'crisisoninfiniteearths', 15:'alexlake', 16:'objectoriented', 17:'henryiv', 18:'disloyal',
    19:'titanquest', 20:'kaprekarconstant', 21:'jamsetjitata', 22:'carryingthefire', 23:'isleofman',
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
        return render(request, 'nth/level4.html', {'player' : player, 'leaderboard':Player.objects.all().order_by('-level', 'last_time')[1:11], 'rank' : getRank(player)})

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

def level6(request):
    if not request.user.is_authenticated: raise Http404("Page Does Not Exist!")

    player = Player.objects.get(user = request.user)
    rank = getRank(player)

    if player.level < 5: raise Http404("Page Does Not Exist!")

    else:
        if player.level == 5:
            player.level = 6
            player.save()
        return render(request, 'nth/level6.html', {'player' : player, 'leaderboard':Player.objects.all().order_by('-level', 'last_time')[1:11], 'rank' : getRank(player)})

def level7(request):
    if not request.user.is_authenticated: raise Http404("Page Does Not Exist!")

    player = Player.objects.get(user = request.user)
    rank = getRank(player)

    if player.level < 6: raise Http404("Page Does Not Exist!")

    else:
        if player.level == 6:
            player.level = 7
            player.save()
        return render(request, 'nth/level7.html', {'player' : player, 'leaderboard':Player.objects.all().order_by('-level', 'last_time')[1:11], 'rank' : getRank(player)})

def level8(request):
    if not request.user.is_authenticated: raise Http404("Page Does Not Exist!")

    player = Player.objects.get(user = request.user)
    rank = getRank(player)

    if player.level < 7: raise Http404("Page Does Not Exist!")

    else:
        if player.level == 7:
            player.level = 8
            player.save()
        return render(request, 'nth/level8.html', {'player' : player, 'leaderboard':Player.objects.all().order_by('-level', 'last_time')[1:11], 'rank' : getRank(player)})

def level9(request):
    if not request.user.is_authenticated: raise Http404("Page Does Not Exist!")

    player = Player.objects.get(user = request.user)
    rank = getRank(player)

    if player.level < 8: raise Http404("Page Does Not Exist!")

    else:
        if player.level == 8:
            player.level = 9
            player.save()
        return render(request, 'nth/level9.html', {'player' : player, 'leaderboard':Player.objects.all().order_by('-level', 'last_time')[1:11], 'rank' : getRank(player)})

def level10(request):
    if not request.user.is_authenticated: raise Http404("Page Does Not Exist!")

    player = Player.objects.get(user = request.user)
    rank = getRank(player)

    if player.level < 9: raise Http404("Page Does Not Exist!")

    else:
        if player.level == 9:
            player.level = 10
            player.save()
        return render(request, 'nth/level10.html', {'player' : player, 'leaderboard':Player.objects.all().order_by('-level', 'last_time')[1:11], 'rank' : getRank(player)})

def level11(request):
    if not request.user.is_authenticated: raise Http404("Page Does Not Exist!")

    player = Player.objects.get(user = request.user)
    rank = getRank(player)

    if player.level < 10: raise Http404("Page Does Not Exist!")

    else:
        if player.level == 10:
            player.level = 11
            player.save()
        return render(request, 'nth/level11.html', {'player' : player, 'leaderboard':Player.objects.all().order_by('-level', 'last_time')[1:11], 'rank' : getRank(player)})

def level12(request):
    if not request.user.is_authenticated: raise Http404("Page Does Not Exist!")

    player = Player.objects.get(user = request.user)
    rank = getRank(player)

    if player.level < 11: raise Http404("Page Does Not Exist!")

    else:
        if player.level == 11:
            player.level = 12
            player.save()
        return render(request, 'nth/level12.html', {'player' : player, 'leaderboard':Player.objects.all().order_by('-level', 'last_time')[1:11], 'rank' : getRank(player)})

def level13(request):
    if not request.user.is_authenticated: raise Http404("Page Does Not Exist!")

    player = Player.objects.get(user = request.user)
    rank = getRank(player)

    if player.level < 12: raise Http404("Page Does Not Exist!")

    else:
        if player.level == 12:
            player.level = 13
            player.save()
        return render(request, 'nth/level13.html', {'player' : player, 'leaderboard':Player.objects.all().order_by('-level', 'last_time')[1:11], 'rank' : getRank(player)})

def level14(request):
    if not request.user.is_authenticated: raise Http404("Page Does Not Exist!")

    player = Player.objects.get(user = request.user)
    rank = getRank(player)

    if player.level < 13: raise Http404("Page Does Not Exist!")

    else:
        if player.level == 13:
            player.level = 14
            player.save()
        return render(request, 'nth/level14.html', {'player' : player, 'leaderboard':Player.objects.all().order_by('-level', 'last_time')[1:11], 'rank' : getRank(player)})

def level15(request):
    if not request.user.is_authenticated: raise Http404("Page Does Not Exist!")

    player = Player.objects.get(user = request.user)
    rank = getRank(player)

    if player.level < 14: raise Http404("Page Does Not Exist!")

    else:
        if player.level == 14:
            player.level = 15
            player.save()
        return render(request, 'nth/level15.html', {'player' : player, 'leaderboard':Player.objects.all().order_by('-level', 'last_time')[1:11], 'rank' : getRank(player)})

def level16(request):
    if not request.user.is_authenticated: raise Http404("Page Does Not Exist!")

    player = Player.objects.get(user = request.user)
    rank = getRank(player)

    if player.level < 15: raise Http404("Page Does Not Exist!")

    else:
        if player.level == 15:
            player.level = 16
            player.save()
        return render(request, 'nth/level16.html', {'player' : player, 'leaderboard':Player.objects.all().order_by('-level', 'last_time')[1:11], 'rank' : getRank(player)})

def level17(request):
    if not request.user.is_authenticated: raise Http404("Page Does Not Exist!")

    player = Player.objects.get(user = request.user)
    rank = getRank(player)

    if player.level < 16: raise Http404("Page Does Not Exist!")

    else:
        if player.level == 16:
            player.level = 17
            player.save()
        return render(request, 'nth/level17.html', {'player' : player, 'leaderboard':Player.objects.all().order_by('-level', 'last_time')[1:11], 'rank' : getRank(player)})

def level18(request):
    if not request.user.is_authenticated: raise Http404("Page Does Not Exist!")

    player = Player.objects.get(user = request.user)
    rank = getRank(player)

    if player.level < 17: raise Http404("Page Does Not Exist!")

    else:
        if player.level == 17:
            player.level = 18
            player.save()
        return render(request, 'nth/level18.html', {'player' : player, 'leaderboard':Player.objects.all().order_by('-level', 'last_time')[1:11], 'rank' : getRank(player)})

def level19(request):
    if not request.user.is_authenticated: raise Http404("Page Does Not Exist!")

    player = Player.objects.get(user = request.user)
    rank = getRank(player)

    if player.level < 18: raise Http404("Page Does Not Exist!")

    else:
        if player.level == 18:
            player.level = 19
            player.save()
        return render(request, 'nth/level19.html', {'player' : player, 'leaderboard':Player.objects.all().order_by('-level', 'last_time')[1:11], 'rank' : getRank(player)})

def level20(request):
    if not request.user.is_authenticated: raise Http404("Page Does Not Exist!")

    player = Player.objects.get(user = request.user)
    rank = getRank(player)

    if player.level < 19: raise Http404("Page Does Not Exist!")

    else:
        if player.level == 19:
            player.level = 20
            player.save()
        return render(request, 'nth/level20.html', {'player' : player, 'leaderboard':Player.objects.all().order_by('-level', 'last_time')[1:11], 'rank' : getRank(player)})

def level21(request):
    if not request.user.is_authenticated: raise Http404("Page Does Not Exist!")

    player = Player.objects.get(user = request.user)
    rank = getRank(player)

    if player.level < 20: raise Http404("Page Does Not Exist!")

    else:
        if player.level == 20:
            player.level = 21
            player.save()
        return render(request, 'nth/level21.html', {'player' : player, 'leaderboard':Player.objects.all().order_by('-level', 'last_time')[1:11], 'rank' : getRank(player)})

def level22(request):
    if not request.user.is_authenticated: raise Http404("Page Does Not Exist!")

    player = Player.objects.get(user = request.user)
    rank = getRank(player)

    if player.level < 21: raise Http404("Page Does Not Exist!")

    else:
        if player.level == 21:
            player.level = 22
            player.save()
        return render(request, 'nth/level22.html', {'player' : player, 'leaderboard':Player.objects.all().order_by('-level', 'last_time')[1:11], 'rank' : getRank(player)})

def level23(request):
    if not request.user.is_authenticated: raise Http404("Page Does Not Exist!")

    player = Player.objects.get(user = request.user)
    rank = getRank(player)

    if player.level < 22: raise Http404("Page Does Not Exist!")

    else:
        if player.level == 22:
            player.level = 23
            player.save()
        return render(request, 'nth/level23.html', {'player' : player, 'leaderboard':Player.objects.all().order_by('-level', 'last_time')[1:11], 'rank' : getRank(player)})

def getRank(player):
    rank = 0
    for p in Player.objects.all().order_by('-level', 'last_time'):
        if p == player: break
        rank = rank + 1
    return rank

def logs(request):
    template_name = 'nth/logs.html'
    return render(request, template_name, {'players':Player.objects.all(), 'count':len(User.objects.filter(is_staff=False))})
