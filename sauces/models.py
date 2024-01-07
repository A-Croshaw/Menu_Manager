from django.db import models
from djrichtextfield.models import RichTextField
from products.models import Product
from django.contrib.auth.models import User

# Choice Fields
TYPE = (
    ("cold_sauce", "Cold Sauce"),
    ("hot_sauce", "Hot Sauce"),
    )

COURSE = (
    ("main", "Main"),
    ("starter", "Starter"),
    ("side", "Side"),
)

UNITS = (
    ('gr', 'gr'),
    ('kg', 'Kg'),
    ('ml', 'ml'),
    ('lt', 'lt'),
    )


class Sauce(models.Model):
    """
    A Model To Create Recipes
    """
    user = models.ForeignKey(
        User,
        related_name="sauce_recipe_user",
        on_delete=models.SET_NULL,
        null=True,
    )
    sauce_name = models.CharField(
        max_length=300,
        null=False,
        blank=False
    )
    sauce_description = models.CharField(
        max_length=500,
        null=False,
        blank=False
    )
    sauce_type = models.CharField(
        max_length=50, choices=TYPE, default="Cold Sauce"
    )
    sauce_course = models.CharField(
        max_length=50, choices=COURSE, default="Side"
    )
    def __str__(self):
        return str(self.sauce_name)


class SauceIngredients(models.Model):
    """
    A Model To Create Ingredients For The Recipes
    """
    sauce = models.ForeignKey(
        Sauce,
        on_delete=models.CASCADE
        )
    sauce_ingredient = models.ForeignKey(
        Product,
        on_delete=models.
        SET_NULL,
        null=True,
        related_name="sauce_ing"
        )
    sauce_quantity = models.DecimalField(
        max_digits=10,
        decimal_places=2
        )
    sauce_unit_type = models.CharField(
        max_length=50,
        choices=UNITS,
        default="gr"
        )

    def __str__(self):
        return str(self.sauce_ingredient)


class SauceMethod(models.Model):
    """
    A Model To create Steps For The Recipe
    """
    sauce = models.ForeignKey(
        Sauce,
        on_delete=models.CASCADE
        )
    sauce_Steps = models.CharField(
        max_length=500,
        null=False,
        blank=False
    )

    def __str__(self):
        return str(self.sauce_Steps)

