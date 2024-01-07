from django.db import models
from djrichtextfield.models import RichTextField
from products.models import Product
from django.contrib.auth.models import User

# Choice Fields
TYPE = (
    ("cold_main", "Cold_main"),
    ("hot_main", "Hot main"),
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
    ('ml', 'ml'),
    ('lt', 'lt'),
    )


class Main(models.Model):
    """
    A Model To Create Main Course Recipes
    """
    user = models.ForeignKey(
        User,
        related_name="main_user",
        on_delete=models.SET_NULL,
        null=True,
    )
    main_name = models.CharField(
        max_length=300,
        null=False,
        blank=False
        )
    main_description = models.CharField(
        max_length=500,
        null=False,
        blank=False
        )
    main_type = models.CharField(
        max_length=50, choices=TYPE, default="Cold Main"
    )
    main_meat_type = models.CharField(
        max_length=50, choices=Meat_TYPE, default="chicken"
    )
    
    class Meta:
        ordering = ["main_name"]

    def __str__(self):
        return str(self.main_name)


class MainIngredients(models.Model):
    """
    A Model To Create Ingredients For The Recipes
    """
    main = models.ForeignKey(
        Main,
        on_delete=models.CASCADE
        )
    main_ingredient = models.ForeignKey(
        Product,
        on_delete=models.
        SET_NULL,
        null=True,
        related_name="main_ing"
        )
    main_quantity = models.DecimalField(
        max_digits=10,
        decimal_places=2
        )
    main_unit_type = models.CharField(
        max_length=50,
        choices=UNITS,
        default="gr"
        )
    
    def __str__(self):
        return str(self.main_ingredient)


class MainMethod(models.Model):
    """
    A Model To create Steps For The Recipe
    """
    main = models.ForeignKey(
        Main,
        on_delete=models.CASCADE
        )
    main_Steps = models.CharField(
        max_length=500,
        null=False,
        blank=False
    )

    def __str__(self):
        return str(self.main_Steps)
