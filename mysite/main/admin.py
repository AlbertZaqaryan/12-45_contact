from django.contrib import admin
from .models import Phone, Contact
# Register your models here.

@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price']
    list_display_links = ['id', 'name']
    search_fields = ['name', 'price']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_name']
    list_display_links = ['id', 'user_name']
    search_fields = ['name']