from django.contrib import admin
from .models import Sport, SportImage

class SportImageInline(admin.TabularInline):
    model = SportImage
    extra = 1

class SportAdmin(admin.ModelAdmin):
    inlines = [SportImageInline]

admin.site.register(Sport, SportAdmin)
