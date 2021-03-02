from .models import Comment, Ticket
from django import forms

class CommentForm(forms.ModelForm):


    class Meta:
        model = Comment
        fields = ('name', 'body')


class CreateTicketForm(forms.ModelForm):

    class Meta:
        model = Ticket
        fields = '__all__'

class UpdateProductForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = '__all__'

