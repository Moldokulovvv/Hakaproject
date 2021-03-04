from django.urls import path

from .views import *

urlpatterns = [
    path('', MainPageView.as_view(), name='home'),
    path('category/<str:slug>/', CategoryDetailView, name='category'),
    path('ticket-detail/<int:pk>/', ticket_detail, name='detail'),
    path('search/', SearchView.as_view(), name='search'),
    path('tickets/create/', TicketCreatedView.as_view(), name="create-ticket"),
    path('tickets/delete/<int:pk>/', TicketDeleteView.as_view(), name='delete-ticket'),
    path('tickets/edit/<int:pk>/', TicketEditView.as_view(), name='edit-ticket'),
    path('blog', blog, name='blog'),



]