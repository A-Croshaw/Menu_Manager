from django.views.generic import TemplateView
from main_courses.models import Main
from main_dishes.models import MainDish
from starters.models import Starter
from starter_dishes.models import StarterDish
from desserts.models import Dessert
from dessert_sauces.models import DessertSauce
from dessert_dishes.models import DessertDish
from sauces.models import Sauce
from sides.models import Side
from menu.models import Menu
from products.models import Product
from django.shortcuts import render


def Index(request):
    """
    View full Main Recipie
    """

    menu = Menu.objects.all()
    main = Main.objects.all()
    main_dish = MainDish.objects.all()
    starter = Starter.objects.all()
    starter_dish = StarterDish.objects.all()
    dessert = Dessert.objects.all()
    dessert_sauces = DessertSauce.objects.all()
    dessert_dish = DessertDish.objects.all()
    sauce = Sauce.objects.all()
    side = Side.objects.all()
    product = Product.objects.all()
    context = {
        "menu": menu,
        "main": main,
        "main_dish": main_dish,
        "starter": starter,
        "starter_dish": starter_dish,
        "dessert": dessert,
        "dessert_sauces": dessert_sauces,
        "dessert_dish": dessert_dish,
        "sauce": sauce,
        "side": side,
        "product": product,

    }

    return render(request, 'home/index.html', context,)
