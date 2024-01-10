from django.db import models
from djrichtextfield.models import RichTextField
from main_courses.models import Main
from sides.models import Side
from sauces.models import Sauce
from django.contrib.auth.models import User


# Choice Fields
TYPE = (
    ("Cold Main", "Cold Main"),
    ("Hot Main", "Hot Main"),
    )


class MainDish(models.Model):
    """
    A Model To Create Main Recipes
    """
    user = models.ForeignKey(
        User,
        related_name="main_dish_user",
        on_delete=models.SET_NULL,
        null=True,
    )
    main_dish_name = models.CharField(
        max_length=300,
        null=False,
        blank=False
        )
    main_dish_description = models.CharField(
        max_length=500,
        null=False,
        blank=False
        )
    main_dish_type = models.CharField(
        max_length=50, choices=TYPE, default="Cold Main"
    )

    class Meta:
        ordering = ["main_dish_name"]

    def __str__(self):
        return str(self.main_dish_name)


class MainDishSauce(models.Model):
    """
    A Model To Create Ingredients For The Recipes
    """
    main_dish = models.ForeignKey(
        MainDish,
        on_delete=models.CASCADE
        )
    main_dish_sauce = models.ForeignKey(
        Sauce,
        on_delete=models.
        SET_NULL,
        null=True,
        related_name="main_sauce"
        )
        
    def __str__(self):
        return str(self.main_dish_sauce)


class MainDishElement(models.Model):
    """
    A Model To Add Elements To A Main Dish
    """
    main_dish = models.ForeignKey(
       MainDish,
        on_delete=models.CASCADE
        )
    main_dish_element = models.ForeignKey(
        Main,
        on_delete=models.
        SET_NULL,
        null=True,
        related_name="main_element"
        )

    def __str__(self):
        return str(self.main_dish_element)


class MainDishSide(models.Model):
    """
    A Model To Add Sides To A Main Dish
    """
    main_dish = models.ForeignKey(
       MainDish,
        on_delete=models.CASCADE
        )
    main_dish_side = models.ForeignKey(
        Side,
        on_delete=models.
        SET_NULL,
        null=True,
        related_name="main_side"
        )

    def __str__(self):
        return str(self.main_dish_side)

