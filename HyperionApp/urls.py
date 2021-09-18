from django.urls import path
from . import views

app_name = "HyperionApp"

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.signin, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('signout/', views.signout, name='signout'),
]
