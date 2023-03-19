from django.urls import path
from . import views

urlpatterns = [
     path('', views.welcome, name='welcome'),
     path('about/', views.about, name='about'),
     path('department/', views.department, name='department'),
     path('homepage/', views.homepage, name='homepage'),
     path('login/', views.loginPage, name='login'),
     path('logout/', views.logoutUser, name='logout'),
     path('signup/', views.signupPage, name='signup'),
     path('signup_successful/', views.signup_success, name='signup_success'),
     path('profile/', views.profile, name='profile'),
     path('news/', views.newsUpdate, name='news'),
     path('upcomingevents/', views.upcomingEvents, name='upcomingevents'),
]