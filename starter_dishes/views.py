from django.http.response import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import (
    login_required, permission_required)
from django.contrib.auth.mixins import (
    PermissionRequiredMixin,
    LoginRequiredMixin)
from django.views.generic import ListView, DeleteView
from django.db.models import Q
from django.contrib import messages
from .models import (
    StarterDish,
    StarterDishSauce,
    StarterDishElement)
from .forms import (
    StarterDishForm,
    StarterDishSauceForm,
    StarterDishElementForm)


class ViewStarterDish(ListView):
    """View All Starter Dishes"""

    template_name = "starter_dishes/starter_dishes.html"
    context_object_name = "starter_dishes"
    model = StarterDish

    def get_queryset(self, **kwargs):
        """
        Starter Dish search function
        """
        starter_dish_search = self.request.GET.get('q')
        if starter_dish_search:
            starter_dish = self.model.objects.filter(
                Q(starter_dish_name__icontains=starter_dish_search)
            )
        else:
            starter_dish = self.model.objects.all()
        return starter_dish


@login_required
@permission_required("starter_dishes.add_starter_dish", raise_exception=True)
def add_starter_dish(request):
    """
    Add Starter Dish function
    """
    form = StarterDishForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            starter_dish = form.save(commit=False)
            starter_dish.starter_dish = starter_dish
            starter_dish.save()
            messages.success(request, 'Starter Successfully Added!')
            return redirect("starter_dish_view", pk=starter_dish.id)
        else:
            return render(request,
                          "starter_dishes/add_starter_dish.html",
                          context={
                              "form": form
                              })
    context = {
        "form": form,
    }
    return render(request, "starter_dishes/add_starter_dish.html", context)


def starter_dish_view(request, pk):
    """
    View full starter dish
    """
    starter_dish = StarterDish.objects.get(id=pk)
    starter_dish_sauce = StarterDishSauce.objects.filter(
        starter_dish=starter_dish)
    starter_dish_element = StarterDishElement.objects.filter(
        starter_dish=starter_dish)

    context = {
        "starter_dish": starter_dish,
        "starter_dish_element": starter_dish_element,
        "starter_dish_sauce": starter_dish_sauce
    }

    return render(request, "starter_dishes/starter_dish_view.html", context,)


@login_required
@permission_required("starter_dishes.edit_starter_dish", raise_exception=True)
def edit_starter_dish(request, pk):
    """
    Updates dish Fields
    """
    starter_dish = StarterDish.objects.get(id=pk)
    form = StarterDishForm(request.POST or None, instance=starter_dish)
    starter_dish_sauce = StarterDishSauce.objects.filter(
        starter_dish=starter_dish)
    starter_dish_element = StarterDishElement.objects.filter(
        starter_dish=starter_dish)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, 'Updated Successfully!')
        return redirect("starter_dish_view", pk=starter_dish.id)

    context = {
        "form": form,
        "starter_dish": starter_dish,
        "starter_dish_sauce": starter_dish_sauce,
        "starter_dish_element": starter_dish_element,
    }

    return render(request, "starter_dishes/edit_starter_dish.html", context)


class StarterDishDelete(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    """
    Deletes starter Dish
    """
    permission_required = "StarterDishDelete"
    model = StarterDish
    success_url = '/starter_dishes/'

    def test_func(self):

        return self.request.user == self.get_object().user


# Starter Dish Element
@login_required
@permission_required("starter_dishes.starter_dish_element", raise_exception=True)
def starter_dish_element(request, pk):
    """
    Add Dish Elements
    """
    starter_dish = StarterDish.objects.get(id=pk)
    starter_dish_sauce = StarterDishSauce.objects.filter(
        starter_dish=starter_dish)
    starter_dish_element = StarterDishElement.objects.filter(
        starter_dish=starter_dish)
    form = StarterDishElementForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            starter_dish_element = form.save(commit=False)
            starter_dish_element.starter_dish = starter_dish
            starter_dish_element.save()
            messages.success(request, 'Element Successfully Added!')
            return redirect(
                "starter_dish_element_details",
                pk=starter_dish_element.id)
        else:
            return render(request,
                          "includes/add_starter_dish_element.html",
                          context={
                              "form": form
                              })

    context = {
        "form": form,
        "starter_dish": starter_dish,
        "starter_dish_sauce": starter_dish_sauce,
        "starter_dish_element": starter_dish_element,
    }

    return render(request, "starter_dishes/starter_dish_element.html", context)


@login_required
@permission_required("starter_dishes.update_starter_dish_element", raise_exception=True)
def update_starter_dish_element(request, pk):
    """
    Updates dish_element Fields
    """
    starter_dish_element = StarterDishElement.objects.get(id=pk)
    form = StarterDishElementForm(
        request.POST or None, instance=starter_dish_element)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, 'Updated Successfully!')
        return redirect(
            "starter_dish_element_details", pk=starter_dish_element.id)

    context = {
        "form": form,
        "starter_dish_element": starter_dish_element
    }

    return render(request, "includes/add_starter_dish_element.html", context)


def starter_dish_element_detail_view(request, pk):
    """
    Displays dish_element Fields After Being Added
    """
    starter_dish_element = get_object_or_404(StarterDishElement, id=pk)
    context = {
        " starter_dish_element":  starter_dish_element
        }
    return render(
        request,
        "includes/ starter_dish_element_details.html", context)


@login_required
@permission_required("starter_dishes.starter_dish_element_details", raise_exception=True)
def starter_dish_element_details(request, pk):
    """
    Displays dish_element Fields for updating
    """
    starter_dish_element = get_object_or_404(StarterDishElement, id=pk)
    context = {
        "starter_dish_element": starter_dish_element
    }
    return render(
        request,
        "includes/starter_dish_element_details.html", context)


@login_required
@permission_required("starter_dishes.add_starter_dish_element", raise_exception=True)
def add_starter_dish_element(request):
    """
    Renders The Form Add Extra dish_element
    """
    form = StarterDishElementForm()
    context = {
        "form": form
    }
    return render(
        request,
        "includes/add_starter_dish_element.html", context)


@login_required
@permission_required("starter_dishes.delete_starter_dish_element", raise_exception=True)
def delete_starter_dish_element(request, pk):
    """
    Deletes Element Field
    """
    starter_dish_element = get_object_or_404(
        StarterDishElement, id=pk)

    if request.method == "POST":
        starter_dish_element.delete()
        messages.success(request, 'Element Deleted')
        return HttpResponse("")

    return HttpResponseNotAllowed(
        [
            "POST",
        ]
    )


# Starter Dish Sauce
@login_required
@permission_required("starter_dishes.starter_dish_sauce", raise_exception=True)
def starter_dish_sauce(request, pk):
    """
    Add Dish Sauces
    """
    starter_dish = StarterDish.objects.get(id=pk)
    starter_dish_sauce = StarterDishSauce.objects.filter(
        starter_dish=starter_dish)
    starter_dish_element = StarterDishElement.objects.filter(
        starter_dish=starter_dish)
    form = StarterDishSauceForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            starter_dish_sauce = form.save(commit=False)
            starter_dish_sauce.starter_dish = starter_dish
            starter_dish_sauce.save()
            messages.success(request, 'Sauce Successfully Added!')
            return redirect(
                "starter_dish_sauce_details", pk=starter_dish_sauce.id)
        else:
            return render(request,
                          "includes/add_starter_dish_sauce.html",
                          context={
                              "form": form
                              })

    context = {
        "form": form,
        "starter_dish": starter_dish,
        "starter_dish_sauce": starter_dish_sauce,
        "starter_dish_element": starter_dish_element,
    }

    return render(
        request,
        "starter_dishes/starter_dish_sauce.html", context)


@login_required
@permission_required("starter_dishes.update_starter_dish_sauce", raise_exception=True)
def update_starter_dish_sauce(request, pk):
    """
    Updates dish sauce Fields
    """
    starter_dish_sauce = StarterDishSauce.objects.get(id=pk)
    form = StarterDishSauceForm(
        request.POST or None, instance=starter_dish_sauce)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, 'Updated Successfully!')
        return redirect(
            "starter_dish_sauce_details", pk=starter_dish_sauce.id)

    context = {
        "form": form,
        "starter_dish_sauce": starter_dish_sauce
    }

    return render(
        request, "includes/add_starter_dish_sauce.html", context)


def starter_dish_sauce_detail_view(request, pk):
    """
    Displays dish sauce Fields After Being Added
    """
    starter_dish_sauce = get_object_or_404(StarterDishSauce, id=pk)
    context = {
        " starter_dish_sauce":  starter_dish_sauce
        }
    return render(
        request, "includes/ starter_dish_sauce_details.html", context)


@login_required
@permission_required("starter_dishes.starter_dish_sauce_details", raise_exception=True)
def starter_dish_sauce_details(request, pk):
    """
    Displays dish sauce Fields for updating
    """
    starter_dish_sauce = get_object_or_404(StarterDishSauce, id=pk)
    context = {
        "starter_dish_sauce": starter_dish_sauce
    }
    return render(
        request, "includes/starter_dish_sauce_details.html", context)


@login_required
@permission_required("starter_dishes.add_starter_dish_sauce", raise_exception=True)
def add_starter_dish_sauce(request):
    """
    Renders The Form Add Extra dish_sauce
    """
    form = StarterDishSauceForm()
    context = {
        "form": form
    }
    return render(
        request, "includes/add_starter_dish_sauce.html", context)


@login_required
@permission_required("starter_dishes.delete_starter_dish_sauce", raise_exception=True)
def delete_starter_dish_sauce(request, pk):
    """
    Deletes Sauce Field
    """
    starter_dish_sauce = get_object_or_404(StarterDishSauce, id=pk)

    if request.method == "POST":
        starter_dish_sauce.delete()
        messages.success(request, 'Step Deleted')
        return HttpResponse("")

    return HttpResponseNotAllowed(
        [
            "POST",
        ]
    )
