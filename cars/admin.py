from django.contrib import admin
from .models import Car, Bicycle

class CarAdmin(admin.ModelAdmin):
    list_display = ('brand','model','year','price')
    search_fields = ('brand',)
    list_filter = ('brand','model','price')

admin.site.register(Car, CarAdmin)
admin.site.register(Bicycle)
