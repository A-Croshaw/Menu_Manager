from django import forms
from .models import DessertSauce, DessertSauceIngredients, DessertSauceMethod


class DessertSauceIngredientForm(forms.ModelForm):
    """Dessert Sauce Ingredient Field Form"""

    class Meta:
        """
        Form Fields
        """
        model = DessertSauceIngredients
        fields = (
                  'dessert_sauce_ingredient',
                  'dessert_sauce_quantity',
                  'dessert_sauce_unit_type',
                  )
        labels = {
            'dessert_sauce_ingredient': 'Ingredient',
            'dessert_sauce_quantity': 'Quantity',
            'dessert_sauce_unit_type': 'Unit',
        }


class DessertSauceForm(forms.ModelForm):
    """Dessert Sauce Setup Form"""

    class Meta:
        """
        Form Fields
        """
        model = DessertSauce
        fields = ("dessert_sauce_name",
                  "dessert_sauce_description",
                  "dessert_sauce_type",
                  )
        widget = {
            "dessert_sauce_description": forms.Textarea(attrs={"rows": 5}),
        }
        labels = {
            "dessert_sauce_name": "Name",
            "dessert_sauce_description": "Description",
            "dessert_sauce_type": "Type",
        }


class DessertSauceMethodForm(forms.ModelForm):
    """Dessert Sauce Method form"""

    class Meta:
        """Form Fields"""
        
        model = DessertSauceMethod
        fields = ("dessert_sauce_Steps",
                  )
        labels = {
            "dessert_sauce_Steps": "Steps",
        }
