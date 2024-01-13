from django.http.response import HttpResponse, HttpResponseNotAllowed
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, DeleteView
from django.db.models import Q
from django.contrib import messages
from .forms import MainIngredientForm, MainForm, MainMethodForm
from .models import Main, MainIngredients, MainMethod


class ViewMain(ListView):
    """View All Mains"""

    template_name = "main_courses/main_courses.html"
    context_object_name = "mains"
    model = Main

    def get_queryset(self, **kwargs):
        """
        Main Course search function
        """
        main_search = self.request.GET.get('q')
        if main_search:
            main = self.model.objects.filter(
                Q(main_name__icontains=main_search) |
                Q(main_type__icontains=main_search)
            )
        else:
            main = self.model.objects.all()
        return main


@login_required
def add_main(request):
    """
    Add Main Course function
    """
    form = MainForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            main = form.save(commit=False)
            main.main = main
            main.save()
            messages.success(request, 'Main Course Successfull!')
            return redirect("main_view", pk=main.id)
        else:
            return render(request,
                          "main_courses/add_main.html",
                          context={
                              "form": form
                              })
    context = {
        "form": form,
    }
    return render(request, "main_courses/add_main.html", context)


def main_view(request, pk):
    """
    View full Main Recipie
    """
    main = Main.objects.get(id=pk)
    main_step = MainMethod.objects.filter(main=main)
    main_ingredients = MainIngredients.objects.filter(main=main)

    context = {
        "main": main,
        "main_ingredients": main_ingredients,
        "main_step": main_step
    }

    return render(request, "main_courses/main_view.html", context,)


def main_ingredients(request, pk):
    """
    Creates Ingredient Fields And Add More Enterys
    """
    main = Main.objects.get(id=pk)
    main_ingredients = MainIngredients.objects.filter(main=main)
    main_step = MainMethod.objects.filter(main=main)
    form = MainIngredientForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            main_ingredient = form.save(commit=False)
            main_ingredient.main = main
            main_ingredient.save()
            messages.success(request, 'Ingredient Successfull Added!')
            return redirect("main_ing_details", pk=main_ingredient.id)
        else:
            return render(request,
                          "includes/add_main_ing.html",
                          context={
                              "form": form
                              })

    context = {
        "form": form,
        "main": main,
        "main_ingredients": main_ingredients,
        "main_step": main_step
    }

    return render(request, "main_courses/main_ingredients.html", context)


def main_method(request, pk):
    """
    Add Recipe Steps
    """
    main = Main.objects.get(id=pk)
    main_step = MainMethod.objects.filter(main=main)
    main_ingredients = MainIngredients.objects.filter(main=main)
    form = MainMethodForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            main_step = form.save(commit=False)
            main_step.main = main
            main_step.save()
            messages.success(request, 'Step Successfull Added!')
            return redirect("main_step_details", pk=main_step.id)
        else:
            return render(request,
                          "includes/add_main_step.html",
                          context={
                              "form": form
                              })

    context = {
        "form": form,
        "main": main,
        "main_step": main_step,
        "main_ingredients": main_ingredients
    }

    return render(request, "main_courses/main_method.html", context)


@login_required
def update_main_ing(request, pk):
    """
    Updates Ingredient Fields
    """
    main_ingredient = MainIngredients.objects.get(id=pk)
    form = MainIngredientForm(request.POST or None, instance=main_ingredient)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, 'Updated Successfull!')
        return redirect("main_ing_details", pk=main_ingredient.id)

    context = {
        "form": form,
        "main_ingredient": main_ingredient
    }

    return render(request, "includes/add_main_ing.html", context)


@login_required
def update_main_step(request, pk):
    """
    Updates step Fields
    """
    main_step = MainMethod.objects.get(id=pk)
    form = MainMethodForm(request.POST or None, instance=main_step)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, 'Updated Successfully!')
        return redirect("main_step_details", pk=main_step.id)

    context = {
        "form": form,
        "main_step": main_step
    }

    return render(request, "includes/add_main_step.html", context)


@login_required
def edit_main(request, pk):
    """
    Updates Main Fields
    """
    main = Main.objects.get(id=pk)
    form = MainForm(request.POST or None, instance=main)
    main_step = MainMethod.objects.filter(main=main)
    main_ingredients = MainIngredients.objects.filter(main=main)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, 'Updated Successfully!')
        return redirect("main_view", pk=main.id)

    context = {
        "form": form,
        "main": main,
        "main_ingredients": main_ingredients,
        "main_step": main_step,
    }

    return render(request, "main_courses/edit_main.html", context)


@login_required
def delete_main_ing(request, pk):
    """
    Deletes Ingredient Fields
    """
    main_ingredient = get_object_or_404(MainIngredients, id=pk)

    if request.method == "POST":
        main_ingredient.delete()
        messages.success(request, 'Ingredient Deleted')
        return HttpResponse("")

    return HttpResponseNotAllowed(
        [
            "POST",
        ]
    )


@login_required
def delete_main_step(request, pk):
    """
    Deletes Step Fields
    """
    main_step = get_object_or_404(MainMethod, id=pk)

    if request.method == "POST":
        main_step.delete()
        messages.success(request, 'Step Deleted')
        return HttpResponse("")

    return HttpResponseNotAllowed(
        [
            "POST",
        ]
    )


class MainDelete(LoginRequiredMixin, DeleteView):
    """
    Deletes Main Course
    """
    model = Main
    success_url = '/main_courses/'

    def test_func(self):

        return self.request.user == self.get_object().user


def main_ing_details(request, pk):
    """
    Displays Ingredient Fields for updating
    """
    main_ingredient = get_object_or_404(MainIngredients, id=pk)
    context = {
        "main_ingredient": main_ingredient
    }
    return render(request, "includes/main_ing_details.html", context)


def main_step_details(request, pk):
    """
    Displays Step Fields for updating
    """
    main_step = get_object_or_404(MainMethod, id=pk)
    context = {
        "main_step": main_step
    }
    return render(request, "includes/main_step_details.html", context)


def main_ing_detail_view(request, pk):
    """
    Displays Ingredient Fields After Being Added
    """
    main_ingredient = get_object_or_404(MainIngredients, id=pk)
    context = {
        "main_ingredient": main_ingredient
        }
    return render(request, "includes/main_ing_details.html", context)


def main_step_detail_view(request, pk):
    """
    Displays Step Fields After Being Added
    """
    main_step = get_object_or_404(MainMethod, id=pk)
    context = {
        " main_step":  main_step
        }
    return render(request, "includes/ main_step_details.html", context)


@login_required
def add_main_ing(request):
    """
    Renders The Form Add Extra Ingredients
    """
    form = MainIngredientForm()
    context = {
        "form": form
    }
    return render(request, "includes/add_main_ing.html", context)


@login_required
def add_main_step(request):
    """
    Renders The Form Add Extra Steps
    """
    form = MainMethodForm()
    context = {
        "form": form
    }
    return render(request, "includes/add_main_step.html", context)
