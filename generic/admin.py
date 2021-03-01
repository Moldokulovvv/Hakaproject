from django.contrib import admin

from .models import *

admin.site.register(Category)
admin.site.register(Ticket)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'ticket', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')
admin.site.register(Comment, CommentAdmin)


