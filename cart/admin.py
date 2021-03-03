from django.contrib import admin

from account.models import User


class UserAdmin(admin.ModelAdmin):

    list_display = ('email', 'is_active', 'name', 'last_name', 'is_superuser', 'is_staff', 'activation_code')
    list_display_links = ('email', 'name', 'last_name')


admin.site.register(User, UserAdmin)