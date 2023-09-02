from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    """Form to Add A Product"""

    class Meta:
        model = Product
        fields = [
            "product_name",
            "product_type",
            "product_freshness",
            "product_cost",
            "product_quantity",
        ]

        labels = {
            "product_name": "Product Name",
            "product_type": "Product Type",
            "product_freshness": "Product Freshness",
            "product_cost": "Product Cost",
            "product_quantity": "Product Quantity",
        }
