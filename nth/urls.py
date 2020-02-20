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
    path('logout/', views.Logout, name = 'Logout'),
]