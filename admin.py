#! coding: utf-8

import models
from django.contrib import admin


class MenuItemInline(admin.TabularInline):
    model = models.MenuItem

    list_display = ['name', 'url']
    search_fields = ['name', 'url', 'title']
    

class MenuAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    search_fields = ['slug', 'name']

    prepopulated_fields = {'slug': ('name',)}
    inlines = [MenuItemInline]


admin.site.register(models.Menu, MenuAdmin)
