from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('login', Login.as_view(), name='login'),
    path('register', Register.as_view(), name='register'),
    path('logout', Logout.as_view(), name='logout'),

    path('detail', Detail.as_view(), name='detail'),
]