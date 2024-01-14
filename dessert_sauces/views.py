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
from .forms import (
    DessertSauceIngredientForm,
    DessertSauceForm,
    DessertSauceMethodForm
    )
from .models import DessertSauce, DessertSauceIngredients, DessertSauceMethod


class ViewDessertSauce(ListView):
    """View All Dessert_sauce"""

    template_name = "dessert_sauces/dessert_sauces.html"
    context_object_name = "dessert_sauces"
    model = DessertSauce

    def get_queryset(self, **kwargs):
        """
        Dessert Sauce search function
        """
        dessert_sauce_search = self.request.GET.get('q')
        if dessert_sauce_search:
            dessert_sauce = self.model.objects.filter(
                Q(dessert_sauce_name__icontains=dessert_sauce_search) |
                Q(dessert_sauce_type__icontains=dessert_sauce_search)
            )
        else:
            dessert_sauce = self.model.objects.all()
        return dessert_sauce


@login_required
@permission_required("dessert_sauces.add_dessert_sauce", raise_exception=True)
def add_dessert_sauce(request):
    """
    Add Dessert Sauce Course function
    """
    form = DessertSauceForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            dessert_sauce = form.save(commit=False)
            dessert_sauce.dessert_sauce = dessert_sauce
            dessert_sauce.save()
            messages.success(request, 'Dessert Sauce Successfully!')
            return redirect("dessert_sauce_view", pk=dessert_sauce.id)
        else:
            return render(request,
                          "dessert_sauces/add_dessert_sauce.html",
                          context={
                              "form": form
                              })
    context = {
        "form": form,
    }
    return render(request, "dessert_sauces/add_dessert_sauce.html", context)


def dessert_sauce_view(request, pk):
    """View full Dessert Sauce Recipie"""

    dessert_sauce = DessertSauce.objects.get(id=pk)
    dessert_sauce_step = DessertSauceMethod.objects.filter(
        dessert_sauce=dessert_sauce)
    dessert_sauce_ingredients = DessertSauceIngredients.objects.filter(
        dessert_sauce=dessert_sauce)

    context = {
        "dessert_sauce": dessert_sauce,
        "dessert_sauce_ingredients": dessert_sauce_ingredients,
        "dessert_sauce_step": dessert_sauce_step
    }

    return render(request, "dessert_sauces/dessert_sauce_view.html", context,)


@login_required
@permission_required("dessert_sauces.edit_dessert_sauce", raise_exception=True)
def edit_dessert_sauce(request, pk):
    """Updates Dessert Sauce Fields"""

    dessert_sauce = DessertSauce.objects.get(id=pk)
    form = DessertSauceForm(request.POST or None, instance=dessert_sauce)
    dessert_sauce_step = DessertSauceMethod.objects.filter(
        dessert_sauce=dessert_sauce)
    dessert_sauce_ingredients = DessertSauceIngredients.objects.filter(
        dessert_sauce=dessert_sauce)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, 'Updated Successfully!')
        return redirect("dessert_sauce_view", pk=dessert_sauce.id)

    context = {
        "form": form,
        "dessert_sauce": dessert_sauce,
        "dessert_sauce_ingredients": dessert_sauce_ingredients,
        "dessert_sauce_step": dessert_sauce_step,
    }

    return render(request, "dessert_sauces/edit_dessert_sauce.html", context)


class DessertSauceDelete(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    """Deletes Dessert Sauce Course"""

    permission_required = "DessertSauceDelete"
    model = DessertSauce
    success_url = '/dessert_sauces/'

    def test_func(self):

        return self.request.user == self.get_object().user


# Dessert Sauce Ingredients
@login_required
@permission_required("dessert_sauces.dessert_sauce_ingredients", raise_exception=True)
def dessert_sauce_ingredients(request, pk):
    """Creates Ingredient Fields And Add More Enterys"""

    dessert_sauce = DessertSauce.objects.get(id=pk)
    dessert_sauce_ingredients = DessertSauceIngredients.objects.filter(
        dessert_sauce=dessert_sauce)
    dessert_sauce_step = DessertSauceMethod.objects.filter(
        dessert_sauce=dessert_sauce)
    form = DessertSauceIngredientForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            dessert_sauce_ingredient = form.save(commit=False)
            dessert_sauce_ingredient.dessert_sauce = dessert_sauce
            dessert_sauce_ingredient.save()
            messages.success(request, 'Ingredient Successfully Added!')
            return redirect(
                "dessert_sauce_ing_details", pk=dessert_sauce_ingredient.id)
        else:
            return render(request,
                          "includes/add_dessert_sauce_ing.html",
                          context={
                              "form": form
                              })

    context = {
        "form": form,
        "dessert_sauce": dessert_sauce,
        "dessert_sauce_ingredients": dessert_sauce_ingredients,
        "dessert_sauce_step": dessert_sauce_step
    }

    return render(
        request, "dessert_sauces/dessert_sauce_ingredients.html", context)


@login_required
@permission_required("dessert_sauces.add_dessert_sauce_ing", raise_exception=True)
def add_dessert_sauce_ing(request):
    """Renders The Form Add Extra Ingredients"""

    form = DessertSauceIngredientForm()
    context = {
        "form": form
    }
    return render(request, "includes/add_dessert_sauce_ing.html", context)


def dessert_sauce_ing_detail_view(request, pk):
    """Displays Ingredient Fields After Being Added"""

    dessert_sauce_ingredient = get_object_or_404(
        DessertSauceIngredients, id=pk)
    context = {
        "dessert_sauce_ingredient": dessert_sauce_ingredient
        }
    return render(request, "includes/dessert_sauce_ing_details.html", context)


@login_required
@permission_required("dessert_sauces.update_dessert_sauce_ing", raise_exception=True)
def update_dessert_sauce_ing(request, pk):
    """Updates Ingredient Fields"""

    dessert_sauce_ingredient = DessertSauceIngredients.objects.get(id=pk)
    form = DessertSauceIngredientForm(
        request.POST or None,
        instance=dessert_sauce_ingredient
        )

    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, 'Updated Successfull!')
        return redirect(
            "dessert_sauce_ing_details", pk=dessert_sauce_ingredient.id)

    context = {
        "form": form,
        "dessert_sauce_ingredient": dessert_sauce_ingredient
    }

    return render(request, "includes/add_dessert_sauce_ing.html", context)


@login_required
@permission_required("dessert_sauces.dessert_sauce_ing_details", raise_exception=True)
def dessert_sauce_ing_details(request, pk):
    """Displays Ingredient Fields for updating"""

    dessert_sauce_ingredient = get_object_or_404(
        DessertSauceIngredients, id=pk)
    context = {
        "dessert_sauce_ingredient": dessert_sauce_ingredient
    }
    return render(request, "includes/dessert_sauce_ing_details.html", context)


@login_required
@permission_required("dessert_sauces.delete_dessert_sauce_ing", raise_exception=True)
def delete_dessert_sauce_ing(request, pk):
    """Deletes Ingredient Fields"""

    dessert_sauce_ingredient = get_object_or_404(
        DessertSauceIngredients, id=pk)

    if request.method == "POST":
        dessert_sauce_ingredient.delete()
        messages.success(request, 'Ingredient Deleted')
        return HttpResponse("")

    return HttpResponseNotAllowed(
        [
            "POST",
        ]
    )


# Dessert Sauce Method
@login_required
@permission_required("dessert_sauces.dessert_sauce_method", raise_exception=True)
def dessert_sauce_method(request, pk):
    """Add Recipe Steps"""

    dessert_sauce = DessertSauce.objects.get(id=pk)
    dessert_sauce_step = DessertSauceMethod.objects.filter(
        dessert_sauce=dessert_sauce)
    dessert_sauce_ingredients = DessertSauceIngredients.objects.filter(
        dessert_sauce=dessert_sauce)
    form = DessertSauceMethodForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            dessert_sauce_step = form.save(commit=False)
            dessert_sauce_step.dessert_sauce = dessert_sauce
            dessert_sauce_step.save()
            messages.success(request, 'Desset Step Successfully Added!')
            return redirect(
                "dessert_sauce_step_details", pk=dessert_sauce_step.id)
        else:
            return render(request,
                          "includes/add_dessert_sauce_step.html",
                          context={
                              "form": form
                              })

    context = {
        "form": form,
        "dessert_sauce": dessert_sauce,
        "dessert_sauce_step": dessert_sauce_step,
        "dessert_sauce_ingredients": dessert_sauce_ingredients
    }

    return render(request, "dessert_sauces/dessert_sauce_method.html", context)


@login_required
@permission_required("dessert_sauces.add_dessert_sauce_step", raise_exception=True)
def add_dessert_sauce_step(request):
    """Renders The Form Add Extra Step"""

    form = DessertSauceMethodForm()
    context = {
        "form": form
    }
    return render(request, "includes/add_dessert_sauce_step.html", context)


def dessert_sauce_step_detail_view(request, pk):
    """Displays Dessert Sauce Fields After Being Added"""

    dessert_sauce_step = get_object_or_404(DessertSauceMethod, id=pk)
    context = {
        " dessert_sauce_step":  dessert_sauce_step
        }
    return render(
        request, "includes/ dessert_sauce_step_details.html", context)


@login_required
@permission_required("dessert_sauces.update_dessert_sauce_step", raise_exception=True)
def update_dessert_sauce_step(request, pk):
    """Updates Step Fields"""

    dessert_sauce_step = DessertSauceMethod.objects.get(id=pk)
    form = DessertSauceMethodForm(
        request.POST or None, instance=dessert_sauce_step)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, 'Updated Successfully!')
        return redirect("dessert_sauce_step_details", pk=dessert_sauce_step.id)

    context = {
        "form": form,
        "dessert_sauce_step": dessert_sauce_step
    }

    return render(request, "includes/add_dessert_sauce_step.html", context)


@login_required
@permission_required("dessert_sauces.update_dessert_sauce_step_details", raise_exception=True)
def dessert_sauce_step_details(request, pk):
    """Displays Step Fields for updating"""

    dessert_sauce_step = get_object_or_404(DessertSauceMethod, id=pk)
    context = {
        "dessert_sauce_step": dessert_sauce_step
    }
    return render(request, "includes/dessert_sauce_step_details.html", context)


@login_required
@permission_required("dessert_sauces.delete_dessert_sauce_step", raise_exception=True)
def delete_dessert_sauce_step(request, pk):
    """Deletes Step Fields"""

    dessert_sauce_step = get_object_or_404(DessertSauceMethod, id=pk)

    if request.method == "POST":
        dessert_sauce_step.delete()
        messages.success(request, 'Step Deleted')
        return HttpResponse("")

    return HttpResponseNotAllowed(
        [
            "POST",
        ]
    )
