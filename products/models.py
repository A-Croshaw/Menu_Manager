from django.db import models
from django.contrib.auth.models import User


# Choice Fields
PRODUCT_TYPE = (
    ("dairy", "Dairy"),
    ("meat", "Meat"),
    ("fish", "Fish"),
    ("dried", "Dried"),
    ("vegetable", "Vegetable"),
    ("fruit", "Fruit"),
    ("n/a", "N/A"),
)


PRODUCT_FRESHNESS = (
    ("frozen", "Frozen"),
    ("fresh", "Fresh"),
    ("n/a", "N/A"),
)


class Product(models.Model):
    """
    A model to create and manage Products
    """
    user = models.ForeignKey(
        User,
        related_name="admin_user",
        on_delete=models.CASCADE
    )
    product_name = models.CharField(max_length=300, null=False, blank=False)
    product_type = models.CharField(
        max_length=50,
        choices=PRODUCT_TYPE,
        default="Dairy"
    )
    product_freshness = models.CharField(
        max_length=50,
        choices=PRODUCT_FRESHNESS,
        default="Dried"
    )
    product_cost = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
    )
    product_quantity = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
    )

    class Meta:
        ordering = ["product_name"]

    def __str__(self):
        return str(self.product_name)
