
from django.urls import path
from . import views
from .views import levels

app_name = 'nth'

urlpatterns = [
    path('', views.Home.as_view(), name='Home'),
    path('loginHunt/', views.Login.as_view(), name='Login'),
    path(levels[1]+'/', views.level1, name = 'Level1'),
    path(levels[2]+'/', views.level2, name = 'Level2'),
    path(levels[3]+'/', views.level3, name = 'Level3'),
    path(levels[4]+'/', views.level4, name = 'Level4'),
    path(levels[5]+'/', views.level5, name = 'Level5'),
    path(levels[6]+'/', views.level6, name = 'Level6'),
    path(levels[7]+'/', views.level7, name = 'Level7'),
    path(levels[8]+'/', views.level8, name = 'Level8'),
    path(levels[9]+'/', views.level9, name = 'Level9'),
    path(levels[10]+'/', views.level10, name = 'Level10'),
    path(levels[11]+'/', views.level11, name = 'Level11'),
    path(levels[12]+'/', views.level12, name = 'Level12'),
    path(levels[13]+'/', views.level13, name = 'Level13'),
    path(levels[14]+'/', views.level14, name = 'Level14'),
    path(levels[15]+'/', views.level15, name = 'Level15'),
    path(levels[16]+'/', views.level16, name = 'Level16'),
    path(levels[17]+'/', views.level17, name = 'Level17'),
    path(levels[18]+'/', views.level18, name = 'Level18'),
    path(levels[19]+'/', views.level19, name = 'Level19'),
    path(levels[20]+'/', views.level20, name = 'Level20'),
    path(levels[21]+'/', views.level21, name = 'Level21'),
    path(levels[22]+'/', views.level22, name = 'Level22'),
    path(levels[23]+'/', views.level23, name = 'Level23'),
    path('logout/', views.Logout, name = 'Logout'),
    path('OLD2/someFiles/renameit/', views.logs, name = 'Logs'),
]

