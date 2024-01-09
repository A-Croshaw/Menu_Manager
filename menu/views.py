from django.http.response import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, DeleteView
from django.db.models import Q
from django.contrib import messages
from .forms import MenuForm, StarterDishItemForm, MainDishItemForm, DessertDishItemForm, SideItemForm, AllegensForm
from .models import Menu, StarterDishItem, MainDishItem, DessertDishItem, SideItem, Allegens


class ViewMenus(ListView):
    """View All Menus"""

    template_name = "menu/menus.html"
    context_object_name = "menu"
    model = Menu

    def get_queryset(self, **kwargs):
        """
        Menu search function
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


def add_menu(request):
    """
    Add Menu function
    """
    form = MenuForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            menu = form.save(commit=False)
            menu.menu = menu
            menu.save()
            return redirect("add_starter_item", pk=menu.id)
        else:
            return render(request,
                          "menu/add_menu.html",
                          context={
                              "form": form
                              })
    context = {
        "form": form,
    }
    return render(request, "menu/add_menu.html", context)


def menu_view(request, pk):
    """
    View full Main Recipie
    """
    menu = Menu.objects.get(id=pk)
    starter_dish_item = StarterDishItem.objects.filter(menu=menu)
    main_dish_item = MainDishItem.objects.filter(menu=menu)
    dessert_dish_item = DessertDishItem.objects.filter(menu=menu)
    side_item = SideItem.objects.filter(menu=menu)
    allegens = Allegens.objects.filter(menu=menu)

    context = {
        "menu": menu,
        "starter_dish_item": starter_dish_item,
        "main_dish_item": main_dish_item,
        "dessert_dish_item": dessert_dish_item,
        "side_item": side_item,
        "allegens": allegens,
    }

    return render(request, "menu/menu_view.html", context,)


# starters
def add_starter_item(request, pk):
    """
    Creates Ingredient Fields And Add More Enterys
    """
    menu = Menu.objects.get(id=pk)
    starter_dish_item = StarterDishItem.objects.filter(menu=menu)
    form = StarterDishItemForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            starter_dish_item = form.save(commit=False)
            starter_dish_item.menu = menu
            starter_dish_item.save()
            return redirect("menu_starter_details", pk=starter_dish_item.id)
        else:
            return render(request,
                          "includes/add_starter.html",
                          context={
                              "form": form
                              })

    context = {
        "form": form,
        "menu": menu,
        "starter_dish_item": starter_dish_item
    }

    return render(request, "menu/menu_starters.html", context)


def menu_starter_details(request, pk):
    """
    Displays Ingredient Fields for updating
    """
    starter_dish_item = get_object_or_404(StarterDishItem, id=pk)
    context = {
        "starter_dish_item": starter_dish_item
    }
    return render(request, "includes/menu_starter_details.html", context)


def add_starter(request):
    """
    Renders The Form Add Extra Ingredients
    """
    form = StarterDishItemForm()
    context = {
        "form": form
    }
    return render(request, "includes/add_starter.html", context)


def menu_starter_view(request, pk):
    """
    Displays Step Fields After Being Added
    """
    starter_dish_item = get_object_or_404(StarterDishItem, id=pk)
    context = {
        "starter_dish_item":  starter_dish_item
        }
    return render(request, "includes/ menu_starter_view.html", context)


# mains
def add_main_item(request, pk):
    """
    Creates Ingredient Fields And Add More Enterys
    """
    menu = Menu.objects.get(id=pk)
    main_dish_item = MainDishItem.objects.filter(menu=menu)
    form = MainDishItemForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            main_dish_item = form.save(commit=False)
            main_dish_item.menu = menu
            main_dish_item.save()
            return redirect("menu_main_details", pk=main_dish_item.id)
        else:
            return render(request,
                          "includes/add_main.html",
                          context={
                              "form": form
                              })

    context = {
        "form": form,
        "menu": menu,
        "main_dish_item": main_dish_item
    }

    return render(request, "menu/menu_mains.html", context)


def menu_main_details(request, pk):
    """
    Displays Ingredient Fields for updating
    """
    main_dish_item = get_object_or_404(MainDishItem, id=pk)
    context = {
        "main_dish_item": main_dish_item
    }
    return render(request, "includes/menu_main_details.html", context)


def add_main(request):
    """
    Renders The Form Add Extra Ingredients
    """
    form = MainDishItemForm()
    context = {
        "form": form
    }
    return render(request, "includes/add_main.html", context)


def menu_main_view(request, pk):
    """
    Displays Step Fields After Being Added
    """
    main_dish_item = get_object_or_404(MainDishItem, id=pk)
    context = {
        "main_dish_item":  main_dish_item
        }
    return render(request, "includes/ menu_main_view.html", context)


# desserts
def add_dessert_item(request, pk):
    """
    Creates Ingredient Fields And Add More Enterys
    """
    menu = Menu.objects.get(id=pk)
    dessert_dish_item = DessertDishItem.objects.filter(menu=menu)
    form = DessertDishItemForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            dessert_dish_item = form.save(commit=False)
            dessert_dish_item.menu = menu
            dessert_dish_item.save()
            return redirect("menu_dessert_details", pk=dessert_dish_item.id)
        else:
            return render(request,
                          "includes/add_dessert.html",
                          context={
                              "form": form
                              })

    context = {
        "form": form,
        "menu": menu,
        "dessert_dish_item": dessert_dish_item
    }

    return render(request, "menu/menu_desserts.html", context)


def menu_dessert_details(request, pk):
    """
    Displays Ingredient Fields for updating
    """
    dessert_dish_item = get_object_or_404(DessertDishItem, id=pk)
    context = {
        "dessert_dish_item": dessert_dish_item
    }
    return render(request, "includes/menu_dessert_details.html", context)


def add_dessert(request):
    """
    Renders The Form Add Extra Ingredients
    """
    form = DessertDishItemForm()
    context = {
        "form": form
    }
    return render(request, "includes/add_dessert.html", context)


def menu_dessert_view(request, pk):
    """
    Displays Step Fields After Being Added
    """
    dessert_dish_item = get_object_or_404(DessertDishItem, id=pk)
    context = {
        "dessert_dish_item":  dessert_dish_item
        }
    return render(request, "includes/ menu_dessert_view.html", context)