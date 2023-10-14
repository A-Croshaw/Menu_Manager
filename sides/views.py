from django.http.response import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, DeleteView
from django.db.models import Q
from django.contrib import messages
from .forms import SideIngredientForm, SideForm, SideMethodForm
from .models import Side, SideIngredients, SideMethod


class ViewSide(ListView):
    """View All Side"""

    template_name = "sides/sides.html"
    context_object_name = "sides"
    model = Side

    def get_queryset(self, **kwargs):
        """
        Side search function
        """
        side_search = self.request.GET.get('q')
        if side_search:
            side = self.model.objects.filter(
                Q(side_name__icontains=side_search) |
                Q(side_type__icontains=side_search)
            )
        else:
            side = self.model.objects.all()
        return side


def add_side(request):
    """
    Add Side Course function
    """
    form = SideForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            side = form.save(commit=False)
            side.side = side
            side.save()
            return redirect("side_view", pk=side.id)
        else:
            return render(request,
                          "sides/add_side.html",
                          context={
                              "form": form
                              })
    context = {
        "form": form,
    }
    return render(request, "sides/add_side.html", context)


def side_view(request, pk):
    """
    View full Side Recipie
    """
    side = Side.objects.get(id=pk)
    side_step = SideMethod.objects.filter(side=side)
    side_ingredients = SideIngredients.objects.filter(side=side)

    context = {
        "side": side,
        "side_ingredients": side_ingredients,
        "side_step": side_step
    }

    return render(request, "sides/side_view.html", context,)


def side_ingredients(request, pk):
    """
    Creates Ingredient Fields And Add More Enterys
    """
    side = Side.objects.get(id=pk)
    side_ingredients = SideIngredients.objects.filter(side=side)
    side_step = SideMethod.objects.filter(side=side)
    form = SideIngredientForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            side_ingredient = form.save(commit=False)
            side_ingredient.side = side
            side_ingredient.save()
            return redirect("side_ing_details", pk=side_ingredient.id)
        else:
            return render(request,
                          "includes/add_side_ing.html",
                          context={
                              "form": form
                              })

    context = {
        "form": form,
        "side": side,
        "side_ingredients": side_ingredients,
        "side_step": side_step
    }

    return render(request, "sides/side_ingredients.html", context)


def side_method(request, pk):
    """
    Add Recipe Steps
    """
    side = Side.objects.get(id=pk)
    side_step = SideMethod.objects.filter(side=side)
    side_ingredients = SideIngredients.objects.filter(side=side)
    form = SideMethodForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            side_step = form.save(commit=False)
            side_step.side = side
            side_step.save()
            return redirect("side_step_details", pk=side_step.id)
        else:
            return render(request,
                          "includes/add_side_step.html",
                          context={
                              "form": form
                              })

    context = {
        "form": form,
        "side": side,
        "side_step": side_step,
        "side_ingredients": side_ingredients
    }

    return render(request, "sides/side_method.html", context)


def update_side_ing(request, pk):
    """
    Updates Ingredient Fields
    """
    side_ingredient = SideIngredients.objects.get(id=pk)
    form = SideIngredientForm(
        request.POST or None,
        instance=side_ingredient
        )

    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, 'Updated Successfull!')
        return redirect("side_ing_details", pk=side_ingredient.id)

    context = {
        "form": form,
        "side_ingredient": side_ingredient
    }

    return render(request, "includes/add_side_ing.html", context)


def update_side_step(request, pk):
    """
    Updates Ingredient Fields
    """
    side_step = SideMethod.objects.get(id=pk)
    form = SideMethodForm(request.POST or None, instance=side_step)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, 'Updated Successfully!')
        return redirect("side_step_details", pk=side_step.id)

    context = {
        "form": form,
        "side_step": side_step
    }

    return render(request, "includes/add_side_ing.html", context)


def edit_side(request, pk):
    """
    Updates Ingredient Fields
    """
    side = Side.objects.get(id=pk)
    form = SideForm(request.POST or None, instance=side)
    side_step = SideMethod.objects.filter(side=side)
    side_ingredients = SideIngredients.objects.filter(side=side)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, 'Updated Successfully!')
        return redirect("side_view", pk=side.id)

    context = {
        "form": form,
        "side": side,
        "side_ingredients": side_ingredients,
        "side_step": side_step,
    }

    return render(request, "sides/edit_side.html", context)


def delete_side_ing(request, pk):
    """
    Deletes Ingredient Fields
    """
    side_ingredient = get_object_or_404(SideIngredients, id=pk)

    if request.method == "POST":
        side_ingredient.delete()
        messages.success(request, 'Ingredient Deleted')
        return HttpResponse("")

    return HttpResponseNotAllowed(
        [
            "POST",
        ]
    )


def delete_side_step(request, pk):
    """
    Deletes Step Fields
    """
    side_step = get_object_or_404(SideMethod, id=pk)

    if request.method == "POST":
        side_step.delete()
        messages.success(request, 'Step Deleted')
        return HttpResponse("")

    return HttpResponseNotAllowed(
        [
            "POST",
        ]
    )


class SideDelete(DeleteView):
    """
    Deletes Side Course
    """
    model = Side
    success_url = '/sides/'

    def test_func(self):

        return self.request.user == self.get_object().user


def side_ing_details(request, pk):
    """
    Displays Ingredient Fields After Being Added
    """
    side_ingredient = get_object_or_404(SideIngredients, id=pk)
    context = {
        "side_ingredient": side_ingredient
    }
    return render(request, "includes/side_ing_details.html", context)


def side_step_details(request, pk):
    """
    Displays Step Fields After Being Added
    """
    side_step = get_object_or_404(SideMethod, id=pk)
    context = {
        "side_step": side_step
    }
    return render(request, "includes/side_step_details.html", context)


def side_ing_detail_view(request, pk):
    """
    Displays Ingredient Fields After Being Added
    """
    side_ingredient = get_object_or_404(SideIngredients, id=pk)
    context = {
        "side_ingredient": side_ingredient
        }
    return render(request, "includes/side_ing_details.html", context)


def side_step_detail_view(request, pk):
    """
    Displays Ingredient Fields After Being Added
    """
    side_step = get_object_or_404(SideMethod, id=pk)
    context = {
        " side_step":  side_step
        }
    return render(request, "includes/ side_step_details.html", context)


def add_side_ing(request):
    """
    Renders The Form Add Extra Ingredients
    """
    form = SideIngredientForm()
    context = {
        "form": form
    }
    return render(request, "includes/add_side_ing.html", context)


def add_side_step(request):
    """
    Renders The Form Add Extra Ingredients
    """
    form = SideMethodForm()
    context = {
        "form": form
    }
    return render(request, "includes/add_side_step.html", context)
