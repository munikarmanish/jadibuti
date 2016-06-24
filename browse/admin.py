from django.contrib import admin

# Register your models here.

from .models import *

class HerbModelAdmin (admin.ModelAdmin):
    list_display = ['eng_name', 'nep_name']
    list_display_links = ['end_name']
    search_fields = ['eng_name', 'nep_name', 'sci_name','description']

    class Meta:
        model = Herb

admin.site.register(Herb, HerbModelAdmin)
