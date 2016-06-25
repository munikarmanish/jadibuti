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

class HerbShopModelAdmin (admin.ModelAdmin):
    list_display = ['name','location']
    list_display_links = ['name']
    list_filter = ['location']
    search_fields = ['name','location','description']

    class Meta:
        model = HerbShop

class SymptomModelAdmin (admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']
    search_fields = ['name']

    class Meta:
        model = Symptom

class DiseaseModelAdmin (admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']
    search_fields = ['name']

    class Meta:
        model = Disease

admin.site.register(Symptom, SymptomModelAdmin)
admin.site.register(Disease, DiseaseModelAdmin)
admin.site.register(HerbShop, HerbShopModelAdmin)
admin.site.register(CarouselImage, CarouselImageModelAdmin)
admin.site.register(Herb, HerbModelAdmin)
admin.site.register (HerbCategory, HerbCategoryModelAdmin)