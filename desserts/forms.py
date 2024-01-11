from django import forms
from .models import Dessert, DessertIngredients, DessertMethod


class DessertIngredientForm(forms.ModelForm):
    """Dessert Ingredient Field Form"""
    
    class Meta:
        """
        Form Fields
        """
        model = DessertIngredients
        fields = (
                  'dessert_ingredient',
                  'dessert_quantity',
                  'dessert_unit_type',
                  )
        labels = {
            'dessert_ingredient': 'Ingredient',
            'dessert_quantity': 'Quantity',
            'dessert_unit_type': 'Unit',
        }


class DessertForm(forms.ModelForm):
    """Dessert Setup Form"""

    class Meta:
        """
        Form Fields
        """
        model = Dessert
        fields = ("dessert_name",
                  "dessert_description",
                  "dessert_type",
                  )
        widget = {
            "dessert_description": forms.Textarea(attrs={"rows": 5}),
        }
        labels = {
            "dessert_name": "Name",
            "dessert_description": "Description",
            "dessert_type": "Type",
        }


class DessertMethodForm(forms.ModelForm):
    """Dessert Method form"""

    class Meta:
        """
        Form Fields
        """

        model = DessertMethod
        fields = ("dessert_Steps",
                  )
        labels = {
            "dessert_Steps": "Steps",
        }
