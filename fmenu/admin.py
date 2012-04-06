from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from fmenu.models import Menu

class MenuAdmin(MPTTModelAdmin):
    list_display = ['title', 'url', 'position', 'active']
    list_editable = ['position', 'active']

admin.site.register(Menu, MenuAdmin)
