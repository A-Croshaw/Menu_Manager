from django.views.generic import TemplateView
from main_courses.models import Main
from starters.models import Starter
from desserts.models import Dessert
from dessert_sauces.models import DessertSauce
from sauces.models import Sauce
from sides.models import Side
from products.models import Product
from django.shortcuts import render


def Index(request):
    """
    View full Main Recipie
    """
    main = Main.objects.all()
    starter = Starter.objects.all()
    dessert = Dessert.objects.all()
    dessert_sauces = DessertSauce.objects.all()
    sauce = Sauce.objects.all()
    side = Side.objects.all()
    product = Product.objects.all()
    context = {
        "main": main,
        "starter": starter,
        "dessert": dessert,
        "sauce": sauce,
        "side": side,
        "product": product,
        "dessert_sauces": dessert_sauces
    }

    return render(request, 'home/index.html', context,)
