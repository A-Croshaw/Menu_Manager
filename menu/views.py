from django.http.response import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DeleteView
from django.db.models import Q
from django.contrib import messages
from .forms import (
    MenuForm, StarterDishItemForm,
    MainDishItemForm, DessertDishItemForm,
    SideItemForm, SauceItemForm)
from .models import (
    Menu, StarterDishItem,
    MainDishItem, DessertDishItem,
    SideItem, SauceItem)


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
                Q(title__icontains=menu_search) |
                Q(menu_type__icontains=menu_search) |
                Q(menu_date__icontains=menu_search)
            )
        else:
            menu = self.model.objects.all()
        return menu


@login_required
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
            messages.success(request, 'Menu Successfully added!')
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
    View full Menu
    """
    menu = Menu.objects.get(id=pk)
    starter_dish_item = StarterDishItem.objects.filter(menu=menu)
    main_dish_item = MainDishItem.objects.filter(menu=menu)
    dessert_dish_item = DessertDishItem.objects.filter(menu=menu)
    side_item = SideItem.objects.filter(menu=menu)
    sauce_item = SauceItem.objects.filter(menu=menu)

    context = {
        "menu": menu,
        "starter_dish_item": starter_dish_item,
        "main_dish_item": main_dish_item,
        "dessert_dish_item": dessert_dish_item,
        "side_item": side_item,
        "sauce_item": sauce_item,
    }

    if menu.menu_type == "specials":
        return render(request, "menu/menu_view_specials.html", context,)
    if menu.menu_type == "early bird":
        return render(request, "menu/menu_view_early.html", context,)
    if menu.menu_type == "à la carte":
        return render(request, "menu/menu_view_à_la_carte.html", context,)


@login_required
def edit_menu(request, pk):
    """
    Updates dish Fields
    """
    menu = Menu.objects.get(id=pk)
    form = MenuForm(request.POST or None, instance=menu)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, 'Updated Successfully!')
        return redirect("add_starter_item", pk=menu.id)

    context = {
        "form": form,
        "menu": menu,
    }

    return render(request, "menu/edit_menu.html", context)


class MenuDelete(LoginRequiredMixin, DeleteView):
    """
    Deletes menu
    """
    model = Menu
    success_url = '/menu/'

    def test_func(self):

        return self.request.user == self.get_object().user


# starters
@login_required
def add_starter_item(request, pk):
    """
    Creates Starter Item And Adds More Enterys
    """
    menu = Menu.objects.get(id=pk)
    starter_dish_item = StarterDishItem.objects.filter(menu=menu)
    form = StarterDishItemForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            starter_dish_item = form.save(commit=False)
            starter_dish_item.menu = menu
            starter_dish_item.save()
            messages.success(request, 'Starter Successfully added!')
            return redirect("menu_starter_details", pk=starter_dish_item.id)
        else:
            return render(request,
                          "includes/add_menu_starter.html",
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
    Displays Starter Item for updating
    """
    starter_dish_item = get_object_or_404(StarterDishItem, id=pk)
    context = {
        "starter_dish_item": starter_dish_item
    }
    return render(request, "includes/menu_starter_details.html", context)


@login_required
def add_menu_starter(request):
    """
    Renders The Form To Add Extra Starter Item
    """
    form = StarterDishItemForm()
    context = {
        "form": form
    }
    return render(request, "includes/add_menu_starter.html", context)


def menu_starter_view(request, pk):
    """
    Displays Starter Item After Being Added
    """
    starter_dish_item = get_object_or_404(StarterDishItem, id=pk)
    context = {
        "starter_dish_item":  starter_dish_item
        }
    return render(request, "includes/ menu_starter_view.html", context)


@login_required
def edit_menu_starter(request, pk):
    """
    Updates menu starter
    """
    starter_dish_item = StarterDishItem.objects.get(id=pk)
    form = StarterDishItemForm(
        request.POST or None, instance=starter_dish_item)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, 'Updated Successfully!')
        return redirect("menu_starter_details", pk=starter_dish_item.id)

    context = {
        "form": form,
        "starter_dish_item": starter_dish_item,
    }

    return render(request, "includes/add_menu_starter.html", context)


@login_required
def delete_starter_dish_item(request, pk):
    """
    Deletes Element Field
    """
    starter_dish_item = get_object_or_404(StarterDishItem, id=pk)

    if request.method == "POST":
        starter_dish_item.delete()
        messages.success(request, 'Starter Item Deleted')
        return HttpResponse("")

    return HttpResponseNotAllowed(
        [
            "POST",
        ]
    )


# mains
@login_required
def add_main_item(request, pk):
    """
    Creates Main Item And Adds More Enterys
    """
    menu = Menu.objects.get(id=pk)
    main_dish_item = MainDishItem.objects.filter(menu=menu)
    form = MainDishItemForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            main_dish_item = form.save(commit=False)
            main_dish_item.menu = menu
            main_dish_item.save()
            messages.success(request, 'Main Successfully added!')
            return redirect("menu_main_details", pk=main_dish_item.id)
        else:
            return render(request,
                          "includes/add_menu_main.html",
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
    Displays Main Items for updating
    """
    main_dish_item = get_object_or_404(MainDishItem, id=pk)
    context = {
        "main_dish_item": main_dish_item
    }
    return render(request, "includes/menu_main_details.html", context)


@login_required
def add_main(request):
    """
    Renders The Form To Add Extra Main Item
    """
    form = MainDishItemForm()
    context = {
        "form": form
    }
    return render(request, "includes/add_menu_main.html", context)


def menu_main_view(request, pk):
    """
    Displays Main Item After Being Added
    """
    main_dish_item = get_object_or_404(MainDishItem, id=pk)
    context = {
        "main_dish_item":  main_dish_item
        }
    return render(request, "includes/ menu_main_view.html", context)


@login_required
def edit_menu_main(request, pk):
    """
    Updates menu main
    """
    main_dish_item = MainDishItem.objects.get(id=pk)
    form = MainDishItemForm(request.POST or None, instance=main_dish_item)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, 'Updated Successfully!')
        return redirect("menu_main_details", pk=main_dish_item.id)

    context = {
        "form": form,
        "main_dish_item": main_dish_item,
    }

    return render(request, "includes/add_menu_main.html", context)


@login_required
def delete_main_dish_item(request, pk):
    """
    Deletes Main Item
    """
    main_dish_item = get_object_or_404(MainDishItem, id=pk)

    if request.method == "POST":
        main_dish_item.delete()
        messages.success(request, 'Main Item Deleted')
        return HttpResponse("")

    return HttpResponseNotAllowed(
        [
            "POST",
        ]
    )


# desserts
@login_required
def add_dessert_item(request, pk):
    """
    Creates Dessert Items And Adds More Enterys
    """
    menu = Menu.objects.get(id=pk)
    dessert_dish_item = DessertDishItem.objects.filter(menu=menu)
    form = DessertDishItemForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            dessert_dish_item = form.save(commit=False)
            dessert_dish_item.menu = menu
            dessert_dish_item.save()
            messages.success(request, 'Dessert Successfully added!')
            return redirect("menu_dessert_details", pk=dessert_dish_item.id)
        else:
            return render(request,
                          "includes/add_menu_dessert.html",
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
    Displays Dessert Items for updating
    """
    dessert_dish_item = get_object_or_404(DessertDishItem, id=pk)
    context = {
        "dessert_dish_item": dessert_dish_item
    }
    return render(request, "includes/menu_dessert_details.html", context)


@login_required
def add_dessert(request):
    """
    Renders The Form To Adds Extra Dessert Item
    """
    form = DessertDishItemForm()
    context = {
        "form": form
    }
    return render(request, "includes/add_menu_dessert.html", context)


def menu_dessert_view(request, pk):
    """
    Displays Dessert Item After Being Added
    """
    dessert_dish_item = get_object_or_404(DessertDishItem, id=pk)
    context = {
        "dessert_dish_item":  dessert_dish_item
        }
    return render(request, "includes/ menu_dessert_view.html", context)


@login_required
def edit_menu_dessert(request, pk):
    """
    Updates menu dessert
    """
    dessert_dish_item = DessertDishItem.objects.get(id=pk)
    form = DessertDishItemForm(
        request.POST or None, instance=dessert_dish_item)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, 'Updated Successfully!')
        return redirect("menu_dessert_details", pk=dessert_dish_item.id)

    context = {
        "form": form,
        "dessert_dish_item": dessert_dish_item,
    }

    return render(request, "includes/add_menu_dessert.html", context)


@login_required
def delete_dessert_dish_item(request, pk):
    """
    Deletes Dessert Item
    """
    dessert_dish_item = get_object_or_404(DessertDishItem, id=pk)

    if request.method == "POST":
        dessert_dish_item.delete()
        messages.success(request, 'Dessert Item Deleted')
        return HttpResponse("")

    return HttpResponseNotAllowed(
        [
            "POST",
        ]
    )


# Sides
@login_required
def add_side_item(request, pk):
    """
    Creates Side Item And Adds More Enterys
    """
    menu = Menu.objects.get(id=pk)
    side_item = SideItem.objects.filter(menu=menu)
    form = SideItemForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            side_item = form.save(commit=False)
            side_item.menu = menu
            side_item.save()
            messages.success(request, 'Side Successfully added!')
            return redirect("menu_side_details", pk=side_item.id)
        else:
            return render(request,
                          "includes/add_menu_side.html",
                          context={
                              "form": form
                              })

    context = {
        "form": form,
        "menu": menu,
        "side_item": side_item
    }

    return render(request, "menu/menu_side.html", context)


def menu_side_details(request, pk):
    """
    Displays Side Items Fields for updating
    """
    side_item = get_object_or_404(SideItem, id=pk)
    context = {
        "side_item": side_item
    }
    return render(request, "includes/menu_side_details.html", context)


@login_required
def add_side(request):
    """
    Renders The Form To Add Extra Side Items
    """
    form = SideItemForm()
    context = {
        "form": form
    }
    return render(request, "includes/add_menu_side.html", context)


def menu_side_view(request, pk):
    """
    Displays Side Item After Being Added
    """
    side_item = get_object_or_404(SideItem, id=pk)
    context = {
        "side_item":  side_item
        }
    return render(request, "includes/ menu_side_view.html", context)


@login_required
def edit_menu_side(request, pk):
    """
    Updates menu side
    """
    side_item = SideItem.objects.get(id=pk)
    form = SideItemForm(request.POST or None, instance=side_item)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, 'Updated Successfully!')
        return redirect("menu_dessert_details", pk=side_item.id)

    context = {
        "form": form,
        "side_item": side_item,
    }

    return render(request, "includes/add_menu_side.html", context)


@login_required
def delete_side_item(request, pk):
    """
    Deletes Side Item
    """
    side_item = get_object_or_404(SideItem, id=pk)

    if request.method == "POST":
        side_item.delete()
        messages.success(request, 'Side Item Deleted')
        return HttpResponse("")

    return HttpResponseNotAllowed(
        [
            "POST",
        ]
    )


# Sauces
@login_required
def add_sauce_item(request, pk):
    """
    Creates sauce Fields And Add More Enterys
    """
    menu = Menu.objects.get(id=pk)
    sauce_item = SauceItem.objects.filter(menu=menu)
    form = SauceItemForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            sauce_item = form.save(commit=False)
            sauce_item.menu = menu
            sauce_item.save()
            messages.success(request, 'Sauce Successfully added!')
            return redirect("menu_sauce_details", pk=sauce_item.id)
        else:
            return render(request,
                          "includes/add_menu_sauce.html",
                          context={
                              "form": form
                              })

    context = {
        "form": form,
        "menu": menu,
        "sauce_item": sauce_item
    }

    return render(request, "menu/menu_sauce.html", context)


def menu_sauce_details(request, pk):
    """
    Displays sauce Fields for updating
    """
    sauce_item = get_object_or_404(SauceItem, id=pk)
    context = {
        "sauce_item": sauce_item
    }
    return render(request, "includes/menu_sauce_details.html", context)


@login_required
def add_sauce(request):
    """
    Renders The Form Add Extra sauces
    """
    form = SauceItemForm()
    context = {
        "form": form
    }
    return render(request, "includes/add_menu_sauce.html", context)


def menu_sauce_view(request, pk):
    """
    Displays sauce Fields After Being Added
    """
    sauce_item = get_object_or_404(SauceItem, id=pk)
    context = {
        "sauce_item":  sauce_item
        }
    return render(request, "includes/ menu_sauce_view.html", context)


@login_required
def edit_menu_sauce(request, pk):
    """
    Updates menu dessert
    """
    sauce_item = SauceItem.objects.get(id=pk)
    form = SauceItemForm(request.POST or None, instance=sauce_item)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, 'Updated Successfully!')
        return redirect("menu_dessert_details", pk=sauce_item.id)

    context = {
        "form": form,
        "sauce_item": sauce_item,
    }

    return render(request, "includes/add_menu_sauce.html", context)


@login_required
def delete_sauce_item(request, pk):
    """
    Deletes Sauce Item
    """
    sauce_item = get_object_or_404(SauceItem, id=pk)

    if request.method == "POST":
        sauce_item.delete()
        messages.success(request, 'Sauce Deleted')
        return HttpResponse("")

    return HttpResponseNotAllowed(
        [
            "POST",
        ]
    )
