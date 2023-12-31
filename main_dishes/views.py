from django.http.response import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, DeleteView
from django.db.models import Q
from django.contrib import messages
from .models import MainDish, MainDishSauce, MainDishElement
from .forms import MainDishForm, MainDishSauceForm, MainDishElementForm

class ViewMainDish(ListView):
    """View All Main Dishes"""

    template_name = "main_dishes/main_dishes.html"
    context_object_name = "main_dishes"
    model = MainDish

    def get_queryset(self, **kwargs):
        """
        Main Dish search function
        """
        main_dish_search = self.request.GET.get('q')
        if main_dish_search:
            main_dish = self.model.objects.filter(
                Q(main_dish_name__icontains=main_dish_search)
            )
        else:
            main_dish = self.model.objects.all()
        return main_dish


def add_main_dish(request):
    """
    Add Main Dish function
    """
    form = MainDishForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            main_dish = form.save(commit=False)
            main_dish.main_dish = main_dish
            main_dish.save()
            return redirect("main_dish_view", pk=main_dish.id)
        else:
            return render(request,
                          "main_dishes/add_main_dish.html",
                          context={
                              "form": form
                              })
    context = {
        "form": form,
    }
    return render(request, "main_dishes/add_main_dish.html", context)


def main_dish_view(request, pk):
    """
    View full Main dish
    """
    main_dish = MainDish.objects.get(id=pk)
    main_dish_sauce = MainDishSauce.objects.filter(main_dish=main_dish)
    main_dish_element = MainDishElement.objects.filter(main_dish=main_dish)

    context = {
        "main_dish": main_dish,
        "main_dish_element": main_dish_element,
        "main_dish_sauce": main_dish_sauce
    }

    return render(request, "main_dishes/main_dish_view.html", context,)


def edit_main_dish(request, pk):
    """
    Updates dish Fields
    """
    main_dish = MainDish.objects.get(id=pk)
    form = MainDishForm(request.POST or None, instance=main_dish)
    main_dish_sauce = MainDishSauce.objects.filter(main_dish=main_dish)
    main_dish_element = MainDishElement.objects.filter(main_dish=main_dish)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, 'Updated Successfully!')
        return redirect("main_dish_view", pk=main_dish.id)

    context = {
        "form": form,
        "main_dish": main_dish,
        "main_dish_sauce": main_dish_sauce,
        "main_dish_element": main_dish_element,
    }

    return render(request, "main_dishes/edit_main_dish.html", context)

class MainDishDelete(DeleteView):
    """
    Deletes main Dish
    """
    model = MainDish
    success_url = '/main_dishes/'

    def test_func(self):

        return self.request.user == self.get_object().user


def main_dish_element(request, pk):
    """
    Add Dish Elements
    """
    main_dish = MainDish.objects.get(id=pk)
    main_dish_sauce = MainDishSauce.objects.filter(main_dish=main_dish)
    main_dish_element = MainDishElement.objects.filter(main_dish=main_dish)
    form = MainDishElementForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            main_dish_element = form.save(commit=False)
            main_dish_element.main_dish = main_dish
            main_dish_element.save()
            return redirect("main_dish_element_details", pk=main_dish_element.id)
        else:
            return render(request,
                          "includes/add_main_dish_element.html",
                          context={
                              "form": form
                              })

    context = {
        "form": form,
        "main_dish": main_dish,
        "main_dish_sauce": main_dish_sauce,
        "main_dish_element": main_dish_element,
    }

    return render(request, "main_dishes/main_dish_element.html", context)


def update_main_dish_element(request, pk):
    """
    Updates dish_element Fields
    """
    main_dish_element = MainDishElement.objects.get(id=pk)
    form = MainDishElementForm(request.POST or None, instance=main_dish_element)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, 'Updated Successfully!')
        return redirect("main_dish_element_details", pk=main_dish_element.id)

    context = {
        "form": form,
        "main_dish_element": main_dish_element
    }

    return render(request, "includes/add_main_dish_element.html", context)


def main_dish_element_detail_view(request, pk):
    """
    Displays dish_element Fields After Being Added
    """
    main_dish_element = get_object_or_404(MainDishElement, id=pk)
    context = {
        " main_dish_element":  main_dish_element
        }
    return render(request, "includes/ main_dish_element_details.html", context)


def main_dish_element_details(request, pk):
    """
    Displays dish_element Fields for updating
    """
    main_dish_element = get_object_or_404(MainDishElement, id=pk)
    context = {
        "main_dish_element": main_dish_element
    }
    return render(request, "includes/main_dish_element_details.html", context)


def add_main_dish_element(request):
    """
    Renders The Form Add Extra dish_element
    """
    form = MainDishElementForm()
    context = {
        "form": form
    }
    return render(request, "includes/add_main_dish_element.html", context)


def delete_main_dish_element(request, pk):
    """
    Deletes Element Field
    """
    main_dish_element = get_object_or_404(MainDishElement, id=pk)

    if request.method == "POST":
        main_dish_element.delete()
        messages.success(request, 'Step Deleted')
        return HttpResponse("")

    return HttpResponseNotAllowed(
        [
            "POST",
        ]
    )


def main_dish_sauce(request, pk):
    """
    Add Dish Sauces
    """
    main_dish = MainDish.objects.get(id=pk)
    main_dish_sauce = MainDishSauce.objects.filter(main_dish=main_dish)
    main_dish_element = MainDishElement.objects.filter(main_dish=main_dish)
    form = MainDishSauceForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            main_dish_sauce = form.save(commit=False)
            main_dish_sauce.main_dish = main_dish
            main_dish_sauce.save()
            return redirect("main_dish_sauce_details", pk=main_dish_sauce.id)
        else:
            return render(request,
                          "includes/add_main_dish_sauce.html",
                          context={
                              "form": form
                              })

    context = {
        "form": form,
        "main_dish": main_dish,
        "main_dish_sauce": main_dish_sauce,
        "main_dish_element": main_dish_element,
    }

    return render(request, "main_dishes/main_dish_sauce.html", context)


def update_main_dish_sauce(request, pk):
    """
    Updates dish sauce Fields
    """
    main_dish_sauce = MainDishSauce.objects.get(id=pk)
    form = MainDishSauceForm(request.POST or None, instance=main_dish_sauce)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, 'Updated Successfully!')
        return redirect("main_dish_sauce_details", pk=main_dish_sauce.id)

    context = {
        "form": form,
        "main_dish_sauce": main_dish_sauce
    }

    return render(request, "includes/add_main_dish_sauce.html", context)


def main_dish_sauce_detail_view(request, pk):
    """
    Displays dish sauce Fields After Being Added
    """
    main_dish_sauce = get_object_or_404(MainDishSauce, id=pk)
    context = {
        " main_dish_sauce":  main_dish_sauce
        }
    return render(request, "includes/ main_dish_sauce_details.html", context)


def main_dish_sauce_details(request, pk):
    """
    Displays dish sauce Fields for updating
    """
    main_dish_sauce = get_object_or_404(MainDishSauce, id=pk)
    context = {
        "main_dish_sauce": main_dish_sauce
    }
    return render(request, "includes/main_dish_sauce_details.html", context)


def add_main_dish_sauce(request):
    """
    Renders The Form Add Extra dish_sauce
    """
    form = MainDishSauceForm()
    context = {
        "form": form
    }
    return render(request, "includes/add_main_dish_sauce.html", context)


def delete_main_dish_sauce(request, pk):
    """
    Deletes Sauce Field
    """
    main_dish_sauce = get_object_or_404(MainDishSauce, id=pk)

    if request.method == "POST":
        main_dish_sauce.delete()
        messages.success(request, 'Step Deleted')
        return HttpResponse("")

    return HttpResponseNotAllowed(
        [
            "POST",
        ]
    )
