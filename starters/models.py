from django.db import models
from djrichtextfield.models import RichTextField
from products.models import Product
from django.contrib.auth.models import User

# Choice Fields
TYPE = (
    ("Soup", "Soup"),
    ("Cold Starter", "Cold Starter"),
    ("Hot Starter", "Hot Starter"),
    )

Meat_TYPE = (
    ('Chicken', 'Chicken'),
    ('Beef', 'Beef'),
    ('Pork', 'Pork'),
    ('Lamb', 'Lamb'),
    ('No Meat', 'No Meat'),
    )

UNITS = (
    ('gr', 'gr'),
    ('kg', 'Kg'),
    ('oz', 'Oz'),
    ('lb', 'Lb'),
    ('tsp', 'tsp'),
    ('Tbsp', 'Tbsp'),
    ('floz', 'floz'),
    ('pint', 'Pint'),
    ('ml', 'ml'),
    ('lt', 'lt'),
    )


class Starter(models.Model):
    """
    A Model To Create Recipes
    """
    user = models.ForeignKey(
        User,
        related_name="starter_recipe_user",
        on_delete=models.SET_NULL,
        null=True,
    )
    starter_name = models.CharField(
        max_length=300,
        null=False,
        blank=False
    )
    starter_description = models.CharField(
        max_length=500,
        null=False,
        blank=False
    )
    starter_type = models.CharField(
        max_length=50, choices=TYPE, default="soup"
    )
    starter_meat_type = models.CharField(
        max_length=50, choices=Meat_TYPE, default="chicken"
    )

    def __str__(self):
        return str(self.starter_name)


class StarterIngredients(models.Model):
    """
    A Model To Create Ingredients For The Recipes
    """
    starter = models.ForeignKey(
        Starter,
        on_delete=models.CASCADE
        )
    starter_ingredient = models.ForeignKey(
        Product,
        on_delete=models.
        SET_NULL,
        null=True,
        related_name="startering"
        )
    starter_quantity = models.DecimalField(
        max_digits=10,
        decimal_places=2
        )
    starter_unit_type = models.CharField(
        max_length=50,
        choices=UNITS,
        default="gr"
        )

    def __str__(self):
        return str(self.starter_ingredient)


class StarterMethod(models.Model):
    """
    A Model To create Steps For The Recipe
    """
    starter = models.ForeignKey(
        Starter,
        on_delete=models.CASCADE
        )
    starter_Steps = models.CharField(
        max_length=500,
        null=False,
        blank=False
    )

    def __str__(self):
        return str(self.starter_Steps)

