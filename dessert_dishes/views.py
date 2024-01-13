from django.http.response import HttpResponse, HttpResponseNotAllowed
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import (
    UserPassesTestMixin,
    LoginRequiredMixin)
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, DeleteView
from django.db.models import Q
from django.contrib import messages
from .models import DessertDish, DessertDishSauce, DessertDishElement
from .forms import (
    DessertDishForm,
    DessertDishSauceForm,
    DessertDishElementForm
    )


class ViewDessertDish(ListView):
    """View All Dessert Dishes"""

    template_name = "dessert_dishes/dessert_dishes.html"
    context_object_name = "dessert_dishes"
    model = DessertDish

    def get_queryset(self, **kwargs):
        """
        Dessert Dish search function
        """
        dessert_dish_search = self.request.GET.get('q')
        if dessert_dish_search:
            dessert_dish = self.model.objects.filter(
                Q(dessert_dish_name__icontains=dessert_dish_search)
            )
        else:
            dessert_dish = self.model.objects.all()
        return dessert_dish


@login_required
def add_dessert_dish(request):
    """Add Dessert Dish function"""

    form = DessertDishForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            dessert_dish = form.save(commit=False)
            dessert_dish.dessert_dish = dessert_dish
            dessert_dish.save()
            messages.success(request, 'Dessert Added Successfully!')
            return redirect("dessert_dish_view", pk=dessert_dish.id)
        else:
            return render(request,
                          "dessert_dishes/add_dessert_dish.html",
                          context={
                              "form": form
                              })
    context = {
        "form": form,
    }
    return render(request, "dessert_dishes/add_dessert_dish.html", context)


def dessert_dish_view(request, pk):
    """View full Dessert dish"""

    dessert_dish = DessertDish.objects.get(id=pk)
    dessert_dish_sauce = DessertDishSauce.objects.filter(
        dessert_dish=dessert_dish)
    dessert_dish_element = DessertDishElement.objects.filter(
        dessert_dish=dessert_dish)

    context = {
        "dessert_dish": dessert_dish,
        "dessert_dish_element": dessert_dish_element,
        "dessert_dish_sauce": dessert_dish_sauce
    }

    return render(request, "dessert_dishes/dessert_dish_view.html", context,)


@login_required
def edit_dessert_dish(request, pk):
    """Updates dish Fields"""

    dessert_dish = DessertDish.objects.get(id=pk)
    form = DessertDishForm(request.POST or None, instance=dessert_dish)
    dessert_dish_sauce = DessertDishSauce.objects.filter(
        dessert_dish=dessert_dish)
    dessert_dish_element = DessertDishElement.objects.filter(
        dessert_dish=dessert_dish)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, 'Updated Successfully!')
        return redirect("dessert_dish_view", pk=dessert_dish.id)

    context = {
        "form": form,
        "dessert_dish": dessert_dish,
        "dessert_dish_sauce": dessert_dish_sauce,
        "dessert_dish_element": dessert_dish_element,
    }

    return render(request, "dessert_dishes/edit_dessert_dish.html", context)


class DessertDishDelete(LoginRequiredMixin, DeleteView):
    """Deletes Dessert Dish"""

    model = DessertDish
    success_url = '/dessert_dishes/'

    def test_func(self):

        return self.request.user == self.get_object().user


# Elements
def dessert_dish_element(request, pk):
    """Add Dish Elements"""

    dessert_dish = DessertDish.objects.get(id=pk)
    dessert_dish_sauce = DessertDishSauce.objects.filter(
        dessert_dish=dessert_dish)
    dessert_dish_element = DessertDishElement.objects.filter(
        dessert_dish=dessert_dish)
    form = DessertDishElementForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            dessert_dish_element = form.save(commit=False)
            dessert_dish_element.dessert_dish = dessert_dish
            dessert_dish_element.save()
            messages.success(request, 'Dish Element Successfully!')
            return redirect(
                "dessert_dish_element_details",
                pk=dessert_dish_element.id)
        else:
            return render(request,
                          "includes/add_dessert_dish_element.html",
                          context={
                              "form": form
                              })

    context = {
        "form": form,
        "dessert_dish": dessert_dish,
        "dessert_dish_sauce": dessert_dish_sauce,
        "dessert_dish_element": dessert_dish_element,
    }

    return render(request, "dessert_dishes/dessert_dish_element.html", context)


@login_required
def update_dessert_dish_element(request, pk):
    """Updates dish_element Fields"""

    dessert_dish_element = DessertDishElement.objects.get(id=pk)
    form = DessertDishElementForm(
        request.POST or None,
        instance=dessert_dish_element)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, 'Updated Successfully!')
        return redirect(
            "dessert_dish_element_details",
            pk=dessert_dish_element.id)

    context = {
        "form": form,
        "dessert_dish_element": dessert_dish_element
    }

    return render(request, "includes/add_dessert_dish_element.html", context)


def dessert_dish_element_detail_view(request, pk):
    """Displays dish_element Fields After Being Added"""

    dessert_dish_element = get_object_or_404(DessertDishElement, id=pk)
    context = {
        " dessert_dish_element":  dessert_dish_element
        }
    return render(
        request,
        "includes/ dessert_dish_element_details.html",
        context)


def dessert_dish_element_details(request, pk):
    """Displays dish_element Fields for updating"""

    dessert_dish_element = get_object_or_404(DessertDishElement, id=pk)
    context = {
        "dessert_dish_element": dessert_dish_element
    }
    return render(
        request,
        "includes/dessert_dish_element_details.html",
        context)


@login_required
def add_dessert_dish_element(request):
    """Renders The Form Add Extra dish_element"""

    form = DessertDishElementForm()
    context = {
        "form": form
    }
    return render(
        request,
        "includes/add_dessert_dish_element.html",
        context)


@login_required
def delete_dessert_dish_element(request, pk):
    """Deletes Element Field"""

    dessert_dish_element = get_object_or_404(
        DessertDishElement,
        id=pk)

    if request.method == "POST":
        dessert_dish_element.delete()
        messages.success(request, 'Element Deleted')
        return HttpResponse("")

    return HttpResponseNotAllowed(
        [
            "POST",
        ]
    )


# Sauces
def dessert_dish_sauce(request, pk):
    """Add Dish Sauces"""

    dessert_dish = DessertDish.objects.get(id=pk)
    dessert_dish_sauce = DessertDishSauce.objects.filter(
        dessert_dish=dessert_dish)
    dessert_dish_element = DessertDishElement.objects.filter(
        dessert_dish=dessert_dish)
    form = DessertDishSauceForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            dessert_dish_sauce = form.save(commit=False)
            dessert_dish_sauce.dessert_dish = dessert_dish
            dessert_dish_sauce.save()
            messages.success(request, 'Dish Sauce Successfully!')
            return redirect(
                "dessert_dish_sauce_details",
                pk=dessert_dish_sauce.id)
        else:
            return render(request,
                          "includes/add_dessert_dish_sauce.html",
                          context={
                              "form": form
                              })

    context = {
        "form": form,
        "dessert_dish": dessert_dish,
        "dessert_dish_sauce": dessert_dish_sauce,
        "dessert_dish_element": dessert_dish_element,
    }

    return render(request, "dessert_dishes/dessert_dish_sauce.html", context)


@login_required
def update_dessert_dish_sauce(request, pk):
    """Updates dish sauce Fields"""

    dessert_dish_sauce = DessertDishSauce.objects.get(id=pk)
    form = DessertDishSauceForm(
        request.POST or None,
        instance=dessert_dish_sauce)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, 'Updated Successfully!')
        return redirect(
            "dessert_dish_sauce_details",
            pk=dessert_dish_sauce.id)

    context = {
        "form": form,
        "dessert_dish_sauce": dessert_dish_sauce
    }

    return render(request, "includes/add_dessert_dish_sauce.html", context)


def dessert_dish_sauce_detail_view(request, pk):
    """Displays dish sauce Fields After Being Added"""

    dessert_dish_sauce = get_object_or_404(DessertDishSauce, id=pk)
    context = {
        " dessert_dish_sauce":  dessert_dish_sauce
        }
    return render(
        request,
        "includes/ dessert_dish_sauce_details.html",
        context)


def dessert_dish_sauce_details(request, pk):
    """Displays dish sauce Fields for updating"""

    dessert_dish_sauce = get_object_or_404(DessertDishSauce, id=pk)
    context = {
        "dessert_dish_sauce": dessert_dish_sauce
    }
    return render(
        request,
        "includes/dessert_dish_sauce_details.html",
        context)


@login_required
def add_dessert_dish_sauce(request):
    """Renders The Form Add Extra dish_sauce"""

    form = DessertDishSauceForm()
    context = {
        "form": form
    }
    return render(request, "includes/add_dessert_dish_sauce.html", context)


@login_required
def delete_dessert_dish_sauce(request, pk):
    """Deletes sauce Field"""

    dessert_dish_sauce = get_object_or_404(DessertDishSauce, id=pk)

    if request.method == "POST":
        dessert_dish_sauce.delete()
        messages.success(request, 'Sauce Deleted')
        return HttpResponse("")

    return HttpResponseNotAllowed(
        [
            "POST",
        ]
    )
