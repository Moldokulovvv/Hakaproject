from datetime import timedelta

from django.core.paginator import Paginator
from django.db.models import Q
from django.utils import timezone

from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView

from generic.forms import CommentForm, CreateTicketForm
from generic.models import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from cart.forms import CartAddTicketForm


# def index(request):
#     return render(request, 'index.html')

class MainPageView(ListView):
    model = Ticket
    template_name = 'index.html'
    context_object_name = 'tickets'
    paginate_by = 100

    def get_template_names(self):
        template_name = super(MainPageView, self).get_template_names()
        filter = self.request.GET.get('filter')
        if filter:
            template_name = 'filter.html'
        return template_name


def get_queryset(self):
    queryset = super().get_queryset()
    search = self.request.GET.get('q')
    filter = self.request.GET.get('filter')
    if search:
        queryset = queryset.filter(Q(title__icontains=search) |
                                   Q(description__icontains=search))
    elif filter:
        start_date = timezone.now() - timedelta(hours=1)
        queryset = queryset.filter(created__gte=start_date)
    return queryset

def CategoryDetailView(request, *args, **kwargs):
    category = kwargs.get('slug', None)
    tickets = Ticket.objects.filter(category_id=category)
    paginator = Paginator(tickets, 1)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'category-detail.html', locals())





# def category_detail(request, slug):
#     category = Category.objects.get(slug=slug)
#     tickets = Ticket.objects.filter(category_id=slug)
#     len_tickets = Ticket.objects.filter(category_id=slug).count()
#     cart_ticket_form = CartAddTicketForm()
#     return render(request, 'category-detail.html', locals())
#


# def ticket_detail(request, pk):
#     ticket = get_object_or_404(Ticket, pk=pk)
#     return render(request, 'ticket-detail.html', locals())

# def search(request):
#     return render(request, 'search.html')

class SearchView(ListView):
    model = Ticket
    template_name = 'search.html'
    context_object_name = 'tickets'


    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('q')
        filter = self.request.GET.get('filter')
        if search:
            queryset = queryset.filter(Q(title__icontains=search) |
                                       Q(description__icontains=search))
        elif filter:
            start_date = timezone.now() - timedelta(hours=10)
            queryset = queryset.filter(created__gte=start_date)
        return queryset




def ticket_detail(request, pk):
    ticket = get_object_or_404(Ticket,pk=pk)
    # List of active comments for this post
    comments = ticket.comments.filter(active=True)
    cart = CartAddTicketForm()


    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.ticket = ticket
            new_comment.email = request.user.email
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request,
                  'ticket-detail.html',
                 {'ticket': ticket,
                  'comments': comments,
                  'comment_form': comment_form, 'cart':cart})


class IsAdminCheckMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and (self.request.user.is_staff or self.request.user.is_superuser)




class TicketCreatedView(IsAdminCheckMixin, CreateView):
    model = Ticket
    form_class = CreateTicketForm
    template_name = 'create_ticket.html'
    success_url = reverse_lazy('home')



class TicketEditView(IsAdminCheckMixin, View):
    def get(self, request, pk):
        ticket = get_object_or_404(Ticket, pk=pk)
        form = CreateTicketForm(instance=ticket)
        return render(request, 'edit_ticket.html', locals())

    def post(self, request, pk):
        ticket = get_object_or_404(Ticket, pk=pk)
        form = CreateTicketForm(instance=ticket, data=request.POST)

        if form.is_valid():
            ticket = form.save()
            return redirect(ticket.get_absolute_url())



class TicketDeleteView(IsAdminCheckMixin,DeleteView):
    model = Ticket
    template_name = 'ticket_delete.html'
    success_url = reverse_lazy('home')




