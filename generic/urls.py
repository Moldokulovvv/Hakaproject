from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('category/<str:slug>/', category_detail, name='category'),
    path('ticket-detail/<int:pk>/', ticket_detail, name='detail'),
    path('search', SearchView, name='search'),

]