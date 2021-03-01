from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path

from account.views import user_login

urlpatterns = [
    path('login/', user_login, name='login'),

]