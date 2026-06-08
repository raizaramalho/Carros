from django.contrib import admin
from cars.models import Car, Brand

class CarAdmin(admin.ModelAdmin):
	list_dsplay = ('model', 'brand', 'factoru_year', 'model_year','plate', 'value','photo')
	search_fields = ('model',)

class BrandAdmin(admin.ModelAdmin):
	list_dsplay = ('name',), 
	search_fields = ('name',)


admin.site.register(Car, CarAdmin)
admin.site.register(Brand, BrandAdmin)
