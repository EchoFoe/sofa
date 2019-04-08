from django.contrib import admin
from .models import *

class About_usImageInline(admin.TabularInline):
    model = About_usImage
    extra = 0

class About_usAdmin(admin.ModelAdmin):
    inlines = [About_usImageInline]
    list_display = ['id', 'description']
    search_fields = ['id']

    class Meta:
        model = About_us


admin.site.register(About_us, About_usAdmin)


class About_usImageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in About_usImage._meta.fields]

    class Meta:
        model = About_usImage


admin.site.register(About_usImage, About_usImageAdmin)