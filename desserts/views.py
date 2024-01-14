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
from .forms import DessertIngredientForm, DessertForm, DessertMethodForm
from .models import Dessert, DessertIngredients, DessertMethod


class ViewDessert(ListView):
    """View All Dessert"""

    template_name = "desserts/desserts.html"
    context_object_name = "desserts"
    model = Dessert

    def get_queryset(self, **kwargs):
        """Dessert search function"""

        dessert_search = self.request.GET.get('q')
        if dessert_search:
            dessert = self.model.objects.filter(
                Q(dessert_name__icontains=dessert_search) |
                Q(dessert_type__icontains=dessert_search)
            )
        else:
            dessert = self.model.objects.all()
        return dessert


@login_required
@permission_required("desserts.add_main_dish", raise_exception=True)
def add_dessert(request):
    """Add Dessert Course function"""

    form = DessertForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            dessert = form.save(commit=False)
            dessert.dessert = dessert
            dessert.save()
            messages.success(request, 'Dessert Added Successfully!')
            return redirect("dessert_view", pk=dessert.id)
        else:
            return render(request,
                          "desserts/add_dessert.html",
                          context={
                              "form": form
                              })
    context = {
        "form": form,
    }
    return render(request, "desserts/add_dessert.html", context)


def dessert_view(request, pk):
    """View full Dessert Recipie"""

    dessert = Dessert.objects.get(id=pk)
    dessert_step = DessertMethod.objects.filter(dessert=dessert)
    dessert_ingredients = DessertIngredients.objects.filter(dessert=dessert)

    context = {
        "dessert": dessert,
        "dessert_ingredients": dessert_ingredients,
        "dessert_step": dessert_step
    }

    return render(request, "desserts/dessert_view.html", context,)


@login_required
@permission_required("desserts.edit_dessert", raise_exception=True)
def edit_dessert(request, pk):
    """Updates Recipe Fields"""

    dessert = Dessert.objects.get(id=pk)
    form = DessertForm(request.POST or None, instance=dessert)
    dessert_step = DessertMethod.objects.filter(dessert=dessert)
    dessert_ingredients = DessertIngredients.objects.filter(dessert=dessert)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, 'Updated Successfully!')
        return redirect("dessert_view", pk=dessert.id)

    context = {
        "form": form,
        "dessert": dessert,
        "dessert_ingredients": dessert_ingredients,
        "dessert_step": dessert_step,
    }

    return render(request, "desserts/edit_dessert.html", context)


class DessertDelete(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    """Deletes Dessert Course"""

    permission_required = "DessertDelete"
    model = Dessert
    success_url = '/desserts/'

    def test_func(self):

        return self.request.user == self.get_object().user


# Dessert Ingredients
@login_required
@permission_required("desserts.dessert_ingredients", raise_exception=True)
def dessert_ingredients(request, pk):
    """Creates Ingredient Fields And Add More Enterys"""

    dessert = Dessert.objects.get(id=pk)
    dessert_ingredients = DessertIngredients.objects.filter(dessert=dessert)
    dessert_step = DessertMethod.objects.filter(dessert=dessert)
    form = DessertIngredientForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            dessert_ingredient = form.save(commit=False)
            dessert_ingredient.dessert = dessert
            dessert_ingredient.save()
            messages.success(request, 'Ingredient Added Successfully!')
            return redirect("dessert_ing_details", pk=dessert_ingredient.id)
        else:
            return render(request,
                          "includes/add_dessert_ing.html",
                          context={
                              "form": form
                              })

    context = {
        "form": form,
        "dessert": dessert,
        "dessert_ingredients": dessert_ingredients,
        "dessert_step": dessert_step
    }

    return render(request, "desserts/dessert_ingredients.html", context)


@login_required
@permission_required("desserts.add_dessert_ing", raise_exception=True)
def add_dessert_ing(request):
    """Renders The Form Add Extra Ingredients"""

    form = DessertIngredientForm()
    context = {
        "form": form
    }
    return render(request, "includes/add_dessert_ing.html", context)


def dessert_ing_detail_view(request, pk):
    """Displays Ingredient Fields After Being Added"""

    dessert_ingredient = get_object_or_404(DessertIngredients, id=pk)
    context = {
        "dessert_ingredient": dessert_ingredient
        }
    return render(request, "includes/dessert_ing_details.html", context)


@login_required
@permission_required("desserts.update_dessert_ing", raise_exception=True)
def update_dessert_ing(request, pk):
    """Updates Ingredient Fields"""

    dessert_ingredient = DessertIngredients.objects.get(id=pk)
    form = DessertIngredientForm(
        request.POST or None,
        instance=dessert_ingredient
        )

    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, 'Updated Successfull!')
        return redirect("dessert_ing_details", pk=dessert_ingredient.id)

    context = {
        "form": form,
        "dessert_ingredient": dessert_ingredient
    }

    return render(request, "includes/add_dessert_ing.html", context)


@login_required
@permission_required("desserts.dessert_ing_details", raise_exception=True)
def dessert_ing_details(request, pk):
    """Displays Ingredient Fields for updating"""

    dessert_ingredient = get_object_or_404(DessertIngredients, id=pk)
    context = {
        "dessert_ingredient": dessert_ingredient
    }
    return render(request, "includes/dessert_ing_details.html", context)


@login_required
@permission_required("desserts.delete_dessert_ing", raise_exception=True)
def delete_dessert_ing(request, pk):
    """Deletes Ingredient Fields"""

    dessert_ingredient = get_object_or_404(DessertIngredients, id=pk)

    if request.method == "POST":
        dessert_ingredient.delete()
        messages.success(request, 'Ingredient Deleted')
        return HttpResponse("")

    return HttpResponseNotAllowed(
        [
            "POST",
        ]
    )


# Dessert method
@login_required
@permission_required("desserts.dessert_method", raise_exception=True)
def dessert_method(request, pk):
    """Add Recipe Steps"""

    dessert = Dessert.objects.get(id=pk)
    dessert_step = DessertMethod.objects.filter(dessert=dessert)
    dessert_ingredients = DessertIngredients.objects.filter(dessert=dessert)
    form = DessertMethodForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            dessert_step = form.save(commit=False)
            dessert_step.dessert = dessert
            dessert_step.save()
            messages.success(request, 'Step Added Successfully!')
            return redirect("dessert_step_details", pk=dessert_step.id)
        else:
            return render(request,
                          "includes/add_dessert_step.html",
                          context={
                              "form": form
                              })

    context = {
        "form": form,
        "dessert": dessert,
        "dessert_step": dessert_step,
        "dessert_ingredients": dessert_ingredients
    }

    return render(request, "desserts/dessert_method.html", context)


@login_required
@permission_required("desserts.add_dessert_step", raise_exception=True)
def add_dessert_step(request):
    """Renders The Form Add Extra Step"""

    form = DessertMethodForm()
    context = {
        "form": form
    }
    return render(request, "includes/add_dessert_step.html", context)


def dessert_step_detail_view(request, pk):
    """Displays Step Fields After Being Added"""

    dessert_step = get_object_or_404(DessertMethod, id=pk)
    context = {
        " dessert_step":  dessert_step
        }
    return render(request, "includes/ dessert_step_details.html", context)


@login_required
@permission_required("desserts.update_dessert_step", raise_exception=True)
def update_dessert_step(request, pk):
    """Updates Step Fields"""

    dessert_step = DessertMethod.objects.get(id=pk)
    form = DessertMethodForm(request.POST or None, instance=dessert_step)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, 'Updated Successfully!')
        return redirect("dessert_step_details", pk=dessert_step.id)

    context = {
        "form": form,
        "dessert_step": dessert_step
    }

    return render(request, "includes/add_dessert_step.html", context)


@login_required
@permission_required("desserts.dessert_step_details", raise_exception=True)
def dessert_step_details(request, pk):
    """Displays Step Fields for updating"""

    dessert_step = get_object_or_404(DessertMethod, id=pk)
    context = {
        "dessert_step": dessert_step
    }
    return render(request, "includes/dessert_step_details.html", context)


@login_required
@permission_required("desserts.delete_dessert_step", raise_exception=True)
def delete_dessert_step(request, pk):
    """Deletes Step Fields"""

    dessert_step = get_object_or_404(DessertMethod, id=pk)

    if request.method == "POST":
        dessert_step.delete()
        messages.success(request, 'Step Deleted')
        return HttpResponse("")

    return HttpResponseNotAllowed(
        [
            "POST",
        ]
    )
