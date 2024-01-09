from django.http.response import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, DeleteView
from django.db.models import Q
from django.contrib import messages
from .forms import MenuForm, StarterDishItemForm, menuDishItemForm, DessertDishItemForm, SideItemForm, AllegensForm
from .models import Menu, StarterDishItem, MainDishItem, DessertDishItem, SideItem, Allegens


class ViewMenus(ListView):
    """View All Menus"""

    template_name = "menu/menus.html"
    context_object_name = "menu"
    model = Menu

    def get_queryset(self, **kwargs):
        """
        Menu Course search function
        """
        menu_search = self.request.GET.get('q')
        if menu_search:
            menu = self.model.objects.filter(
                Q(menu_title__icontains=menu_search) |
                Q(menu_type__icontains=menu_search) |
                Q(menu_date__icontains=menu_search)
            )
        else:
            menu = self.model.objects.all()
        return menu
