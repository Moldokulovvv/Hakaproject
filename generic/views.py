from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from generic.models import *


def index(request):
    return render(request, 'index.html')

def category_detail(request, slug):
    category = Category.objects.get(slug=slug)
    tickets = Ticket.objects.filter(category_id=slug)
    return render(request, 'category-detail.html', locals())

def ticket_detail(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    return render(request, 'ticket-detail.html', locals())

# def search(request):
#     return render(request, 'search.html')

class SearchView(ListView):
    model = Ticket
    template_name = 'search.html'
    context_object_name = 'tickets'

    def get_template_names(self):
        template_name = super(SearchView, self).get_template_names()
        search = self.request.GET.get.get('')
        return template_name

