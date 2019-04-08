from django.contrib import admin
from .models import *

class GuaranteesAdmin(admin.ModelAdmin):
    list_display = ['id', 'description']
    search_fields = ['id']

    class Meta:
        model = Guarantees


admin.site.register(Guarantees, GuaranteesAdmin)