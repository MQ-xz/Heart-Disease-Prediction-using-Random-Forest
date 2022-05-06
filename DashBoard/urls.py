from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('login', Login.as_view(), name='login'),
    path('register', Register.as_view(), name='register'),
    path('logout', Logout.as_view(), name='logout'),

    path('dashboard', CheckHealth.as_view(), name='dashboard'),
    path('history', HistoryView.as_view(), name='history'),
    path('user', Users.as_view(), name='users'),
    path('user/<int:pk>', UserDetail.as_view(), name='userDetail'),
]