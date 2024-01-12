from django.db import models
from djrichtextfield.models import RichTextField
from starters.models import Starter
from sauces.models import Sauce
from django.contrib.auth.models import User


# Choice Fields
TYPE = (
    ("Cold Starter", "Cold Starter"),
    ("Hot Starter", "Hot Starter"),
    )


class StarterDish(models.Model):
    """
    A Model To Create starter Recipes
    """
    starter_dish_name = models.CharField(
        max_length=300,
        null=False,
        blank=False
        )
    starter_dish_description = models.CharField(
        max_length=500,
        null=False,
        blank=False
        )
    starter_dish_type = models.CharField(
        max_length=50, choices=TYPE, default="Cold starter"
    )

    class Meta:
        ordering = ["starter_dish_name"]

    def __str__(self):
        return str(self.starter_dish_name)


class StarterDishSauce(models.Model):
    """
    A Model To Create Ingredients For The Recipes
    """
    starter_dish = models.ForeignKey(
        StarterDish,
        on_delete=models.CASCADE
        )
    starter_dish_sauce = models.ForeignKey(
        Sauce,
        on_delete=models.
        SET_NULL,
        null=True,
        related_name="starter_sauce"
        )
        
    def __str__(self):
        return str(self.starter_dish_sauce)


class StarterDishElement(models.Model):
    """
    A Model To Add Elements To A starter Dish
    """
    starter_dish = models.ForeignKey(
       StarterDish,
        on_delete=models.CASCADE
        )
    starter_dish_element = models.ForeignKey(
        Starter,
        on_delete=models.
        SET_NULL,
        null=True,
        related_name="starter_element"
        )

    def __str__(self):
        return str(self.starter_dish_element)



