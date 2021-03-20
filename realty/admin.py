from django.contrib import admin

from .models import Realty, RealtyImage, Client, Category


@admin.register(Realty)
class RealtyAdmin(admin.ModelAdmin):
    class RealtyImageAdmin(admin.TabularInline):
        verbose_name_plural = "Realty images"
        model = RealtyImage
        extra = 1
        classes = ['collapse']

    inlines = [RealtyImageAdmin]


admin.site.register(Client)
admin.site.register(Category)
