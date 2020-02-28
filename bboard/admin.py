from django.contrib import admin

from .models import Bb, Category


class BbAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'price', 'published', 'category']
    list_display_links = ['title', 'content']
    search_fields = ['title', 'content']
    empty_value_display = '-empty-'

admin.site.register(Bb, BbAdmin)
admin.site.register(Category)