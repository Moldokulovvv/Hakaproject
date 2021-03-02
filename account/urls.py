from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path

from account.views import *

urlpatterns = [
    path('login/', SigningView.as_view(), name='login'),
    path('register/', RegistrationView.as_view(), name='register'),
    path('successfully_register/', SuccessfullyRegistrationView.as_view(), name='successful-registration'),
    path('activation/', ActivationView.as_view(), name='activation'),
    path('logout/', LogoutView.as_view(), name='logout'),
]