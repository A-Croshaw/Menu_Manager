from django.db import models
from django.contrib.auth.models import User
from starter_dishes.models import StarterDish
from main_dishes.models import MainDish
from dessert_dishes.models import DesertDish
from sides.models import Side

# Choice fields
ITEM_TYPES = (
    ("starter", "Starter"),
    ("main", "Main"),
    ("desert", "Desert"),
    ("drink", "Drink"),
    ("side", "Side")
)


class Menu(models.Model):
    """ Model to create a menu """
    user = models.ForeignKey(User,related_name="menu_user",on_delete=models.SET_NULL,null=True,)
    title = models.CharField(max_length=25)
    menu_date = models.DateTimeField(auto_now_add=True)
    date_updated= models.DateTimeField(auto_now=True)

    class Meta:
        """ Order by title """
        ordering = ['title']

    def __str__(self):
        return str(self.name)


class StarterDishItem(models.Model):
    """ A Model to create starter menu items """
    menu = models.ForeignKey(Menu,on_delete=models.CASCADE)
    starter_dish = models.ForeignKey(StarterDish, on_delete=models.CASCADE, related_name="starter_dish_item")
    starter_price = models.FloatField(default=0.00)
    
    class Meta:
        """ Order by starter_dish """
        ordering = ['starter_dish']

    def __str__(self):
        return str(self.name)


class MainDishItem(models.Model):
    """ A Model to create main menu items """
    menu = models.ForeignKey(Menu,on_delete=models.CASCADE)
    main_dish = models.ForeignKey(MainDish, on_delete=models.CASCADE, related_name="main_dish_item")
    main_price = models.FloatField(default=0.00)
    
    class Meta:
        """ Order by main_dish """
        ordering = ['main_dish']

    def __str__(self):
        return str(self.name)

        
class DessertDishItem(models.Model):
    """ A Model to create starter menu items """
    menu = models.ForeignKey(Menu,on_delete=models.CASCADE)
    dessert_dish = models.ForeignKey(DessertDish, on_delete=models.CASCADE, related_name="dessert_dish_item")
    dessert_price = models.FloatField(default=0.00)
    
    class Meta:
        """ Order by dessert_dish """
        ordering = ['dessert_dish']

    def __str__(self):
        return str(self.name)


class SideItem(models.Model):
    """
    A Model to create starter menu items
    """
    menu = models.ForeignKey(Menu,on_delete=models.CASCADE)
    side = models.ForeignKey(Side, on_delete=models.CASCADE, related_name="side_item")
    side_price = models.FloatField(default=0.00)
    
    class Meta:
        """ Order by side """
        ordering = ['side']

    def __str__(self):
        return str(self.name)


class Allegens(models.Model):
    menu = models.ForeignKey(Menu,on_delete=models.CASCADE)
    allegens = models.CharField(max_length=50, choices=ALLEGENS, default="Gluten")

    def __str__(self):
        return str(self.allegens)