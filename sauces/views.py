from django.http.response import HttpResponse, HttpResponseNotAllowed
from django.contrib.auth.decorators import (
    login_required, permission_required)
from django.contrib.auth.mixins import (
    PermissionRequiredMixin,
    LoginRequiredMixin)
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, DeleteView
from django.db.models import Q
from django.contrib import messages
from .forms import SauceIngredientForm, SauceForm, SauceMethodForm
from .models import Sauce, SauceIngredients, SauceMethod


class ViewSauce(ListView):
    """View All sauces"""

    template_name = "sauces/sauces.html"
    context_object_name = "sauces"
    model = Sauce

    def get_queryset(self, **kwargs):
        """
        Sauce search function
        """
        sauce_search = self.request.GET.get('q')
        if sauce_search:
            sauce = self.model.objects.filter(
                Q(sauce_name__icontains=sauce_search) |
                Q(sauce_type__icontains=sauce_search)
            )
        else:
            sauce = self.model.objects.all()
        return sauce


@login_required
@permission_required("sauces.add_sauce", raise_exception=True)
def add_sauce(request):
    """
    Add Sauce function
    """
    form = SauceForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            sauce = form.save(commit=False)
            sauce.sauce = sauce
            sauce.save()
            messages.success(request, 'Sauce Successfully Added!')
            return redirect("sauce_view", pk=sauce.id)
        else:
            return render(request,
                          "sauces/add_sauce.html",
                          context={
                              "form": form
                              })
    context = {
        "form": form,
    }
    return render(request, "sauces/add_sauce.html", context)


def sauce_view(request, pk):
    """
    View full Sauce Recipie
    """
    sauce = Sauce.objects.get(id=pk)
    sauce_step = SauceMethod.objects.filter(sauce=sauce)
    sauce_ingredients = SauceIngredients.objects.filter(sauce=sauce)

    context = {
        "sauce": sauce,
        "sauce_ingredients": sauce_ingredients,
        "sauce_step": sauce_step
    }

    return render(request, "sauces/sauce_view.html", context,)


@login_required
@permission_required("sauces.edit_sauce", raise_exception=True)
def edit_sauce(request, pk):
    """
    Updates Recipie Fields
    """
    sauce = Sauce.objects.get(id=pk)
    form = SauceForm(request.POST or None, instance=sauce)
    sauce_step = SauceMethod.objects.filter(sauce=sauce)
    sauce_ingredients = SauceIngredients.objects.filter(sauce=sauce)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, 'Updated Successfully!')
        return redirect("sauce_view", pk=sauce.id)

    context = {
        "form": form,
        "sauce": sauce,
        "sauce_ingredients": sauce_ingredients,
        "sauce_step": sauce_step,
    }

    return render(request, "sauces/edit_sauce.html", context)


class SauceDelete(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    """
    Deletes Sauce Course
    """
    permission_required = "SauceDeleteDelete"
    model = Sauce
    success_url = '/sauces/'

    def test_func(self):

        return self.request.user == self.get_object().user


# Sauce Ingredients
@login_required
@permission_required("sauces.sauce_ingredients", raise_exception=True)
def sauce_ingredients(request, pk):
    """
    Creates Ingredient Fields And Add More Enterys
    """
    sauce = Sauce.objects.get(id=pk)
    sauce_ingredients = SauceIngredients.objects.filter(sauce=sauce)
    sauce_step = SauceMethod.objects.filter(sauce=sauce)
    form = SauceIngredientForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            sauce_ingredient = form.save(commit=False)
            sauce_ingredient.sauce = sauce
            sauce_ingredient.save()
            messages.success(request, 'Ingredient Successfully Added!')
            return redirect("sauce_ing_details", pk=sauce_ingredient.id)
        else:
            return render(request,
                          "includes/add_sauce_ing.html",
                          context={
                              "form": form
                              })

    context = {
        "form": form,
        "sauce": sauce,
        "sauce_ingredients": sauce_ingredients,
        "sauce_step": sauce_step
    }

    return render(request, "sauces/sauce_ingredients.html", context)


@login_required
@permission_required("sauces.add_sauce_ing", raise_exception=True)
def add_sauce_ing(request):
    """
    Renders The Form Add Extra Ingredients
    """
    form = SauceIngredientForm()
    context = {
        "form": form
    }
    return render(request, "includes/add_sauce_ing.html", context)


def sauce_ing_detail_view(request, pk):
    """
    Displays Ingredient Fields After Being Added
    """
    sauce_ingredient = get_object_or_404(SauceIngredients, id=pk)
    context = {
        "sauce_ingredient": sauce_ingredient
        }
    return render(request, "includes/sauce_ing_details.html", context)


@login_required
@permission_required("sauces.update_sauce_ing", raise_exception=True)
def update_sauce_ing(request, pk):
    """
    Updates Ingredient Fields
    """
    sauce_ingredient = SauceIngredients.objects.get(id=pk)
    form = SauceIngredientForm(
        request.POST or None,
        instance=sauce_ingredient
        )

    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, 'Updated Successfull!')
        return redirect("sauce_ing_details", pk=sauce_ingredient.id)

    context = {
        "form": form,
        "sauce_ingredient": sauce_ingredient
    }

    return render(request, "includes/add_sauce_ing.html", context)


@login_required
@permission_required("sauces.sauce_ing_details", raise_exception=True)
def sauce_ing_details(request, pk):
    """
    Displays Ingredient Fields for updating
    """
    sauce_ingredient = get_object_or_404(SauceIngredients, id=pk)
    context = {
        "sauce_ingredient": sauce_ingredient
    }
    return render(request, "includes/sauce_ing_details.html", context)


@login_required
@permission_required("sauces.delete_sauce_ing", raise_exception=True)
def delete_sauce_ing(request, pk):
    """
    Deletes Ingredient Fields
    """
    sauce_ingredient = get_object_or_404(SauceIngredients, id=pk)

    if request.method == "POST":
        sauce_ingredient.delete()
        messages.success(request, 'Ingredient Deleted')
        return HttpResponse("")

    return HttpResponseNotAllowed(
        [
            "POST",
        ]
    )


@login_required
@permission_required("sauces.sauce_method", raise_exception=True)
def sauce_method(request, pk):
    """
    Add Recipe Steps
    """
    sauce = Sauce.objects.get(id=pk)
    sauce_step = SauceMethod.objects.filter(sauce=sauce)
    sauce_ingredients = SauceIngredients.objects.filter(sauce=sauce)
    form = SauceMethodForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            sauce_step = form.save(commit=False)
            sauce_step.sauce = sauce
            sauce_step.save()
            messages.success(request, 'Step Successfully Added!')
            return redirect("sauce_step_details", pk=sauce_step.id)
        else:
            return render(request,
                          "includes/add_sauce_step.html",
                          context={
                              "form": form
                              })

    context = {
        "form": form,
        "sauce": sauce,
        "sauce_step": sauce_step,
        "sauce_ingredients": sauce_ingredients
    }

    return render(request, "sauces/sauce_method.html", context)


@login_required
@permission_required("sauces.add_sauce_step", raise_exception=True)
def add_sauce_step(request):
    """
    Renders The Form Add Extra Steps
    """
    form = SauceMethodForm()
    context = {
        "form": form
    }
    return render(request, "includes/add_sauce_step.html", context)


def sauce_step_detail_view(request, pk):
    """
    Displays Step Fields After Being Added
    """
    sauce_step = get_object_or_404(SauceMethod, id=pk)
    context = {
        " sauce_step":  sauce_step
        }
    return render(request, "includes/ sauce_step_details.html", context)


@login_required
@permission_required("sauces.update_sauce_step", raise_exception=True)
def update_sauce_step(request, pk):
    """
    Updates step Fields
    """
    sauce_step = SauceMethod.objects.get(id=pk)
    form = SauceMethodForm(request.POST or None, instance=sauce_step)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, 'Updated Successfully!')
        return redirect("sauce_step_details", pk=sauce_step.id)

    context = {
        "form": form,
        "sauce_step": sauce_step
    }

    return render(request, "includes/add_sauce_step.html", context)


@login_required
@permission_required("sauces.sauce_step_details", raise_exception=True)
def sauce_step_details(request, pk):
    """
    Displays Step Fields for updating
    """
    sauce_step = get_object_or_404(SauceMethod, id=pk)
    context = {
        "sauce_step": sauce_step
    }
    return render(request, "includes/sauce_step_details.html", context)


@login_required
@permission_required("sauces.delete_sauce_step(", raise_exception=True)
def delete_sauce_step(request, pk):
    """
    Deletes Step Fields
    """
    sauce_step = get_object_or_404(SauceMethod, id=pk)

    if request.method == "POST":
        sauce_step.delete()
        messages.success(request, 'Step Deleted')
        return HttpResponse("")

    return HttpResponseNotAllowed(
        [
            "POST",
        ]
    )
