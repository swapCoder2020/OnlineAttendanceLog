from django.contrib import admin
from .models import Users

@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'contact')
    ordering = ('first_name',)
    search_fields = ('username', 'first_name', 'email', 'contact')