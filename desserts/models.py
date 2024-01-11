from django.db import models
from djrichtextfield.models import RichTextField
from products.models import Product
from django.contrib.auth.models import User


# Choice Fields
TYPE = (
    ("Cold Dessert", "Cold Dessert"),
    ("Hot Dessert", "Hot Dessert"),
    )


UNITS = (
    ('gr', 'gr'),
    ('Kg', 'Kg'),
    ('ml', 'ml'),
    ('lt', 'lt'),
    )


class Dessert(models.Model):
    """A Model To Create Dessert Recipes"""

    user = models.ForeignKey(
        User,
        related_name="dessert_user",
        on_delete=models.SET_NULL,
        null=True,
    )
    dessert_name = models.CharField(
        max_length=300,
        null=False,
        blank=False
        )
    dessert_description = models.CharField(
        max_length=500,
        null=False,
        blank=False
        )
    dessert_type = models.CharField(
        max_length=50, choices=TYPE,
        default="Cold Dessert"
    )
    class Meta:
        ordering = ["dessert_name"]

    def __str__(self):
        return str(self.dessert_name)


class DessertIngredients(models.Model):
    """A Model To Create Ingredients For The Recipes"""

    dessert = models.ForeignKey(
        Dessert,
        on_delete=models.CASCADE
        )
    dessert_ingredient = models.ForeignKey(
        Product,
        on_delete=models.
        SET_NULL,
        null=True,
        related_name="dessert_ing"
        )
    dessert_quantity = models.DecimalField(
        max_digits=10,
        decimal_places=2
        )
    dessert_unit_type = models.CharField(
        max_length=50,
        choices=UNITS,
        default="gr"
        )

    def __str__(self):
        return str(self.dessert_ingredient)


class DessertMethod(models.Model):
    """A Model To Create Steps For The Recipe"""

    dessert = models.ForeignKey(
        Dessert,
        on_delete=models.CASCADE
        )
    dessert_Steps = models.CharField(
        max_length=500,
        null=False,
        blank=False
    )

    def __str__(self):
        return str(self.dessert_Steps)
