from django.contrib import admin
from .models import *
from import_export.admin import ImportExportActionModelAdmin
from import_export import resources
from import_export import fields
from import_export.widgets import ForeignKeyWidget

class SofaImageInline(admin.TabularInline):
    model = SofaImage
    extra = 0

    class SofaCategoryAdmin(admin.ModelAdmin):
        list_display = [field.name for field in SofaCategory._meta.fields]
        list_filter = ['name', 'id']
        search_fields = ['name', 'id']

        class Meta:
            model = SofaCategory

    admin.site.register(SofaCategory, SofaCategoryAdmin)


class SofaResource(resources.ModelResource):
    category = fields.Field(column_name='category', attribute='category',
                            widget=ForeignKeyWidget(SofaCategory, 'name'))

    class Meta:
        model = Sofa


class SofaAdmin(ImportExportActionModelAdmin):
    resource_class = SofaResource
    # list_display = [field.name for field in Product._meta.fields if field.name != "id"]
    list_display = ['id', 'name', 'price', 'category',
                    'description_S', 'is_active', 'created']
    inlines = [SofaImageInline]
    list_filter = ['category']
    search_fields = ['name', 'id']

    class Meta:
        model = Sofa


admin.site.register(Sofa, SofaAdmin)


class SofaImageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in SofaImage._meta.fields]

    class Meta:
        model = SofaImage


admin.site.register(SofaImage, SofaImageAdmin)