from django.contrib import admin
from .models import DescriptionVersion
# Register your models here.
class VersionAdmin(admin.ModelAdmin):
    list_display=['name']

admin.site.register(DescriptionVersion,VersionAdmin)