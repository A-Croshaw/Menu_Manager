from django.db import models
from djrichtextfield.models import RichTextField
from products.models import Product
from django.contrib.auth.models import User

# Choice Fields
TYPE = (
    ("Cold Sauce", "Cold Sauce"),
    ("Hot Sauce", "Hot Sauce"),
    )

UNITS = (
    ('gr', 'gr'),
    ('Kg', 'Kg'),
    ('Oz', 'Oz'),
    ('lb', 'lSb'),
    ('tsp', 'tsp'),
    ('Tbsp', 'Tbsp'),
    ('floz', 'floz'),
    ('Pint', 'Pint'),
    ('ml', 'ml'),
    ('lt', 'lt'),
    )


class DessertSauce(models.Model):
    """
    A Model To Create Dessert_sauce Recipes
    """
    user = models.ForeignKey(
        User,
        related_name="dessert_sauce_user",
        on_delete=models.SET_NULL,
        null=True,
    )
    dessert_sauce_name = models.CharField(
        max_length=300,
        null=False,
        blank=False
        )
    dessert_sauce_description = models.CharField(
        max_length=500,
        null=False,
        blank=False
        )
    dessert_sauce_type = models.CharField(
        max_length=50, choices=TYPE, default="old Dessert_sauce"
    )

    class Meta:
        ordering = ["dessert_sauce_name"]

    def __str__(self):
        return str(self.dessert_sauce_name)


class DessertSauceIngredients(models.Model):
    """
    A Model To Create Ingredients For The Recipes
    """
    dessert_sauce = models.ForeignKey(
        DessertSauce,
        on_delete=models.CASCADE
        )
    dessert_sauce_ingredient = models.ForeignKey(
        Product,
        on_delete=models.
        SET_NULL,
        null=True,
        related_name="dessert_sauceing"
        )
    dessert_sauce_quantity = models.DecimalField(
        max_digits=10,
        decimal_places=2
        )
    dessert_sauce_unit_type = models.CharField(
        max_length=50,
        choices=UNITS,
        default="gr"
        )

    def __str__(self):
        return str(self.dessert_sauce_ingredient)


class DessertSauceMethod(models.Model):
    """
    A Model To Create Steps For The Recipe
    """
    dessert_sauce = models.ForeignKey(
        DessertSauce,
        on_delete=models.CASCADE
        )
    dessert_sauce_Steps = models.CharField(
        max_length=500,
        null=False,
        blank=False
    )

    def __str__(self):
        return str(self.dessert_sauce_Steps)
