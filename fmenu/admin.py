from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from fmenu.models import Menu

class MenuAdmin(MPTTModelAdmin):
    list_display = ['title', 'url', 'position']

admin.site.register(Menu, MenuAdmin)