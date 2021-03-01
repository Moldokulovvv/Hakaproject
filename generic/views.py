from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from generic.forms import CommentForm
from generic.models import *


def index(request):
    return render(request, 'index.html')

def category_detail(request, slug):
    category = Category.objects.get(slug=slug)
    tickets = Ticket.objects.filter(category_id=slug)
    return render(request, 'category-detail.html', locals())

# def ticket_detail(request, pk):
#     ticket = get_object_or_404(Ticket, pk=pk)
#     return render(request, 'ticket-detail.html', locals())

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



def ticket_detail(request, pk):
    ticket = get_object_or_404(Ticket,pk=pk)
    # List of active comments for this post
    comments = ticket.comments.filter(active=True)

    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.ticket = ticket
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request,
                  'ticket-detail.html',
                 {'ticket': ticket,
                  'comments': comments,
                  'comment_form': comment_form})

