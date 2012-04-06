from django import template
from fmenu.models import Menu

register = template.Library()

def show_menu(name):
    Item = Menu.objects.get(url=name)
    menu = Item.get_descendants()
    return {'menu': menu}

register.inclusion_tag('menu.html')(show_menu)
