from django.db import models
from djrichtextfield.models import RichTextField
from desserts.models import Dessert
from dessert_sauces.models import DessertSauce
from django.contrib.auth.models import User


# Choice Fields
TYPE = (
    ("Cold Dessert", "Cold Dessert"),
    ("Hot Dessert", "Hot Dessert"),
    )


class DessertDish(models.Model):
    """
    A Model To Create Dessert Recipes
    """
    user = models.ForeignKey(
        User,
        related_name="dessert_dish_user",
        on_delete=models.SET_NULL,
        null=True,
    )
    dessert_dish_name = models.CharField(
        max_length=300,
        null=False,
        blank=False
        )
    dessert_dish_description = models.CharField(
        max_length=500,
        null=False,
        blank=False
        )
    dessert_dish_type = models.CharField(
        max_length=50, choices=TYPE, default="Cold Dessert"
    )

    class Meta:
        ordering = ["dessert_dish_name"]

    def __str__(self):
        return str(self.dessert_dish_name)


class DessertDishSauce(models.Model):
    """
    A Model To Create Ingredients For The Recipes
    """
    dessert_dish = models.ForeignKey(
        DessertDish,
        on_delete=models.CASCADE
        )
    dessert_dish_sauce = models.ForeignKey(
        DessertSauce,
        on_delete=models.
        SET_NULL,
        null=True,
        related_name="dessert_sauce"
        )
        
    def __str__(self):
        return str(self.dessert_dish_sauce)


class DessertDishElement(models.Model):
    """
    A Model To Add Elements To A Dessert Dish
    """
    dessert_dish = models.ForeignKey(
       DessertDish,
        on_delete=models.CASCADE
        )
    dessert_dish_element = models.ForeignKey(
        Dessert,
        on_delete=models.
        SET_NULL,
        null=True,
        related_name="dessert_element"
        )

    def __str__(self):
        return str(self.dessert_dish_element)
