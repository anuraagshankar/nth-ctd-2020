from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import Player
from django.db.utils import IntegrityError

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
        return render(request, self.template_name)
    def post(self, request):
        try:
            user = User()
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.username = request.POST['username']
            user.set_password(request.POST['password'])
            user.email = request.POST['email']
            user.save()
            player = Player()
            player.user = user
            player.mobile_number = request.POST['mobile_number']
            player.college = request.POST['college']
            player.save()
        except IntegrityError:
            return HttpResponse("User Exists!")
        return render(request, self.template_name)

class Login(View):
    template_name = 'nth/login.html'
    def get(self, request):
        if request.user.is_authenticated:
            try:
                player = Player.objects.get(user = request.user)
                return redirect('/' + levels[player.level])
            except:
                logout(request)
                return render(request, self.template_name)
        else: return render(request, self.template_name)
    def post(self, request):
        user = authenticate(username = request.POST['username'], password = request.POST['password'])
        if user is not None:
            login(request, user)
            player = Player.objects.get(user = request.user)
            return redirect('/' + levels[player.level])
        else: return HttpResponse("Invalid Credentials!")

def Logout(request):
    logout(request)
    return redirect('/')

def level1(request):
    return render(request, 'nth/level1.html')

def level2(request):
    return render(request, 'nth/level2.html')

def level3(request):
    player = Player.objects.get(user = request.user)
    if player.level < 2: return redirect('/' + levels[player.level])
    else:
        if player.level == 2:
            player.level = 3
            player.save()
        return render(request, 'nth/level3.html')

def level4(request):
    player = Player.objects.get(user = request.user)
    if player.level < 3: return redirect('/' + levels[player.level])
    else:
        if player.level == 3:
            player.level = 4
            player.save() 
        return render(request, 'nth/level4.html')

def level5(request):
    player = Player.objects.get(user = request.user)
    if player.level < 4: return redirect('/' + levels[player.level])
    else:
        if player.level == 4:
            player.level = 5
            player.save()
        return render(request, 'nth/level5.html')

