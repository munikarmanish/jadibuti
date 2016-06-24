from django.contrib import admin

# Register your models here.

from .models import *

class HerbModelAdmin (admin.ModelAdmin):
    list_display = ['eng_name','nep_name']
    list_display_links = ['eng_name']
    search_fields = ['eng_name', 'nep_name', 'sci_name','description']

    class Meta:
        model = Herb

class HerbCategoryModelAdmin (admin.ModelAdmin):
	list_display = ['name']
	list_display_links = ['name']
	search_fields = ['name']

	class Meta:
		model = HerbCategory

class CarouselImageModelAdmin (admin.ModelAdmin):
    list_display = ['caption']
    list_display_links = ['caption']
    list_filter = ['show']
    search_fields = ['caption', 'description']

    class Meta:
        model = CarouselImage


admin.site.register(CarouselImage, CarouselImageModelAdmin)
admin.site.register(Herb, HerbModelAdmin)
admin.site.register (HerbCategory, HerbCategoryModelAdmin)