#! coding: utf-8

import models

def context(request):
    menus = models.Menu.objects.filter()
    context = {
        'menu': {}
    }
    for menu in menus:
        context['menu'][menu.slug] = menu
    return context
