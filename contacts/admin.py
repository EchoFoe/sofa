from django.contrib import admin
from .models import *

class ContactsAdmin(admin.ModelAdmin):
    list_display = ['id', 'phone', 'email']
    search_fields = ['email']

    class Meta:
        model = Contacts


admin.site.register(Contacts, ContactsAdmin)