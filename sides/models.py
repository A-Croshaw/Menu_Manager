from django.db import models
from djrichtextfield.models import RichTextField
from products.models import Product
from django.contrib.auth.models import User


# Choice Fields
TYPE = (
    ("Cold Side", "Cold Side"),
    ("Hot Side", "Hot Side"),
    )


UNITS = (
    ('gr', 'gr'),
    ('kg', 'Kg'),
    ('ml', 'ml'),
    ('lt', 'lt'),
    )


class Side(models.Model):
    """
    A Model To Create Recipes
    """
    user = models.ForeignKey(
        User,
        related_name="side_recipe_user",
        on_delete=models.SET_NULL,
        null=True,
    )
    side_name = models.CharField(
        max_length=300,
        null=False,
        blank=False
    )
    side_description = models.CharField(
        max_length=500,
        null=False,
        blank=False
    )
    side_type = models.CharField(
        max_length=50, choices=TYPE, default="soup"
    )

    def __str__(self):
        return str(self.side_name)


class SideIngredients(models.Model):
    """
    A Model To Create Ingredients For The Recipes
    """
    side = models.ForeignKey(
        Side,
        on_delete=models.CASCADE
        )
    side_ingredient = models.ForeignKey(
        Product,
        on_delete=models.
        SET_NULL,
        null=True,
        related_name="side_ing"
        )
    side_quantity = models.DecimalField(
        max_digits=10,
        decimal_places=2
        )
    side_unit_type = models.CharField(
        max_length=50,
        choices=UNITS,
        default="gr"
        )

    def __str__(self):
        return str(self.side_ingredient)


class SideMethod(models.Model):
    """
    A Model To create Steps For The Recipe
    """
    side = models.ForeignKey(
        Side,
        on_delete=models.CASCADE
        )
    side_Steps = models.CharField(
        max_length=500,
        null=False,
        blank=False
    )

    def __str__(self):
        return str(self.side_Steps)
