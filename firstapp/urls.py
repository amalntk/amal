from django.urls import path
from firstapp import views
urlpatterns = [
    path('index',views.index,name='index'),
    path('login.html',views.login,name='login'),
    path('bmi.html',views.bmic,name='bmi'),
    path('register.html',views.register,name='register'),
    path('',views.welcome,name='welcome'),
    path('welcome.html',views.welcome,name='logout'),
    path('home',views.index,name='home')
    
]