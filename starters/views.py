from django.http.response import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import (
    UserPassesTestMixin,
    LoginRequiredMixin)
from django.views.generic import ListView, DeleteView
from django.db.models import Q
from django.contrib import messages
from .forms import StarterIngredientForm, StarterForm, StarterMethodForm
from .models import Starter, StarterIngredients, StarterMethod


class ViewStarter(ListView):
    """View All starters"""

    template_name = "starters/starters.html"
    context_object_name = "starters"
    model = Starter

    def get_queryset(self, **kwargs):
        """
        Starter search function
        """
        starter_search = self.request.GET.get('q')
        if starter_search:
            starter = self.model.objects.filter(
                Q(starter_name__icontains=starter_search) |
                Q(starter_type__icontains=starter_search)
            )
        else:
            starter = self.model.objects.all()
        return starter


@login_required
def add_starter(request):
    """
    Add starter Course function
    """
    form = StarterForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            starter = form.save(commit=False)
            starter.starter = starter
            starter.save()
            return redirect("starter_view", pk=starter.id)
            return render(
                messages.success(request, 'Starter Successfully Added!'))
        else:
            return render(request,
                          "starters/add_starter.html",
                          context={
                              "form": form
                              })
    context = {
        "form": form,
    }
    return render(request, "starters/add_starter.html", context)


def starter_view(request, pk):
    """
    View full Starter Recipie
    """
    starter = Starter.objects.get(id=pk)
    starter_step = StarterMethod.objects.filter(starter=starter)
    starter_ingredients = StarterIngredients.objects.filter(starter=starter)

    context = {
        "starter": starter,
        "starter_ingredients": starter_ingredients,
        "starter_step": starter_step
    }

    return render(request, "starters/starter_view.html", context,)


@login_required
def starter_ingredients(request, pk):
    """
    Creates Ingredient Fields And Add More Enterys
    """
    starter = Starter.objects.get(id=pk)
    starter_ingredients = StarterIngredients.objects.filter(starter=starter)
    starter_step = StarterMethod.objects.filter(starter=starter)
    form = StarterIngredientForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            starter_ingredient = form.save(commit=False)
            starter_ingredient.starter = starter
            starter_ingredient.save()
            return redirect("starter_ing_details", pk=starter_ingredient.id)
        else:
            return render(request,
                          "includes/add_starter_ing.html",
                          context={
                              "form": form
                              })
        return render(messages.success(
            request, 'Ingredient Successfully Added!'
            ))

    context = {
        "form": form,
        "starter": starter,
        "starter_ingredients": starter_ingredients,
        "starter_step": starter_step
    }

    return render(request, "starters/starter_ingredients.html", context)


def starter_method(request, pk):
    """
    Add Recipe Steps
    """
    starter = Starter.objects.get(id=pk)
    starter_step = StarterMethod.objects.filter(starter=starter)
    starter_ingredients = StarterIngredients.objects.filter(starter=starter)
    form = StarterMethodForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            starter_step = form.save(commit=False)
            starter_step.starter = starter
            starter_step.save()
            return redirect("starter_step_details", pk=starter_step.id)
            return render(messages.success(
                request, 'Step Successfully Added!'))
        else:
            return render(request,
                          "includes/add_starter_step.html",
                          context={
                              "form": form
                              })

    context = {
        "form": form,
        "starter": starter,
        "starter_step": starter_step,
        "starter_ingredients": starter_ingredients
    }

    return render(request, "starters/starter_method.html", context)


@login_required
def update_starter_ing(request, pk):
    """
    Updates Ingredient Fields
    """
    starter_ingredient = StarterIngredients.objects.get(id=pk)
    form = StarterIngredientForm(
        request.POST or None,
        instance=starter_ingredient
        )

    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, 'Updated Successfull!')
        return redirect("starter_ing_details",  pk=starter_ingredient.id,)

    context = {
        "form": form,
        "starter_ingredient": starter_ingredient
    }

    return render(request, "includes/add_starter_ing.html", context)


@login_required
def update_starter_step(request, pk):
    """
    Updates step Fields
    """
    starter_step = StarterMethod.objects.get(id=pk)
    form = StarterMethodForm(request.POST or None, instance=starter_step)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, 'Updated Successfull!')
        return redirect("starter_step_details", pk=starter_step.id)

    context = {
        "form": form,
        "starter_step": starter_step
    }

    return render(request, "includes/add_starter_step.html", context)


@login_required
def edit_starter(request, pk):
    """
    Updates Ingredient Fields
    """
    starter = Starter.objects.get(id=pk)
    form = StarterForm(request.POST or None, instance=starter)
    starter_step = StarterMethod.objects.filter(starter=starter)
    starter_ingredients = StarterIngredients.objects.filter(starter=starter)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, 'Updated Successfull!')
        return redirect("starter_view", pk=starter.id)

    context = {
        "form": form,
        "starter": starter,
        "starter_ingredients": starter_ingredients,
        "starter_step": starter_step,
    }

    return render(request, "starters/edit_starter.html", context)


@login_required
def delete_starter_ing(request, pk):
    """
    Deletes Ingredient Fields
    """
    starter_ingredient = get_object_or_404(StarterIngredients, id=pk)

    if request.method == "POST":
        starter_ingredient.delete()
        messages.success(request, 'Ingredient Deleted')
        return HttpResponse("")

    return HttpResponseNotAllowed(
        [
            "POST",
        ]
    )


@login_required
def delete_starter_step(request, pk):
    """
    Deletes Step Fields
    """
    starter_step = get_object_or_404(StarterMethod, id=pk)

    if request.method == "POST":
        starter_step.delete()
        messages.success(request, 'Step Deleted')
        return HttpResponse("")

    return HttpResponseNotAllowed(
        [
            "POST",
        ]
    )


class StarterDelete(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    """
    Deletes Starter Course
    """
    model = Starter
    success_url = '/starters/'

    def test_func(self):

        return self.request.user == self.get_object().user


def starter_ing_details(request, pk):
    """
    Displays Ingredient Fields for updating
    """
    starter_ingredient = get_object_or_404(StarterIngredients, id=pk)
    context = {
        "starter_ingredient": starter_ingredient
    }
    return render(request, "includes/starter_ing_details.html", context)


def starter_step_details(request, pk):
    """
    Displays Step Fields for updating
    """
    starter_step = get_object_or_404(StarterMethod, id=pk)
    context = {
        "starter_step": starter_step
    }
    return render(request, "includes/starter_step_details.html", context)


def starter_ing_detail_view(request, pk):
    """
    Displays Ingredient Fields After Being Added
    """
    starter_ingredient = get_object_or_404(StarterIngredients, id=pk)
    context = {
        "starter_ingredient": starter_ingredient
        }
    return render(request, "includes/starter_ing_details.html", context)


def starter_step_detail_view(request, pk):
    """
    Displays Ingredient Fields After Being Added
    """
    starter_step = get_object_or_404(StarterMethod, id=pk)
    context = {
        " starter_step":  starter_step
        }
    return render(request, "includes/ starter_step_details.html", context)


@login_required
def add_starter_ing(request):
    """
    Renders The Form Add Extra Ingredients
    """
    form = StarterIngredientForm()
    context = {
        "form": form
    }
    return render(request, "includes/add_starter_ing.html", context)


@login_required
def add_starter_step(request):
    """
    Renders The Form Add Extra Step
    """
    form = StarterMethodForm()
    context = {
        "form": form
    }
    return render(request, "includes/add_starter_step.html", context)
