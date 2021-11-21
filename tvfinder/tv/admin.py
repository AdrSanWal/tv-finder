from django.contrib import admin

from .models import Gender, Director, Tv


class GenderAdmin(admin.ModelAdmin):
    list_display = ('gender',)
    search_fields = ('gender',)
    list_filter = ('gender',)
    readonly_fields = ('created', 'updated')


class DirectorAdmin(admin.ModelAdmin):
    list_display = ('name', 'birth')
    search_fields = ('name',)
    list_filter = ('name',)
    readonly_fields = ('created', 'updated')


class TvAdmin(admin.ModelAdmin):
    list_display = ('title', 'tv_type', 'year', 'rating')
    search_fields = ('title', 'year', 'tv_type')
    list_filter = ('tv_type',)
    readonly_fields = ('created', 'updated')


admin.site.register(Gender, GenderAdmin)
admin.site.register(Director, DirectorAdmin)
admin.site.register(Tv, TvAdmin)
