from django.views.generic import TemplateView
from main_courses.models import Main
from starters.models import Starter
from desserts.models import Dessert
from django.shortcuts import render



def Index(request):
    """
    View full Main Recipie
    """
    main = Main.objects.all()
    starter = Starter.objects.all()
    dessert = Dessert.objects.all()

    context = {
        "main": main,
        "starter": starter,
        "dessert": dessert
    }

    return render(request, 'home/index.html', context,)
