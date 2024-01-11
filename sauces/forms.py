from django import forms
from .models import Sauce, SauceIngredients, SauceMethod


class SauceIngredientForm(forms.ModelForm):
    """
    Sauce ingredient field form
    """
    class Meta:
        """
        Form Fields
        """
        model = SauceIngredients
        fields = (
                  'sauce_ingredient',
                  'sauce_quantity',
                  'sauce_unit_type',
                  )
        labels = {
            'sauce_ingredient': 'Ingredient',
            'sauce_quantity': 'Quantity',
            'sauce_unit_type': 'Unit',
        }


class SauceForm(forms.ModelForm):
    """
    Sauce setup form
    """
    class Meta:
        """
        Form Fields
        """
        model = Sauce
        fields = ("sauce_name",
                  "sauce_description",
                  "sauce_type",
                  "sauce_course",
                  )
        widget = {
            "sauce_description": forms.Textarea(attrs={"rows": 5}),
        }
        labels = {
            "sauce_name": "Name",
            "sauce_description": "Description",
            "sauce_type": "Type",
            "sauce_course": "Sauce Course",
        }


class SauceMethodForm(forms.ModelForm):
    """
    Sauce Method form
    """
    class Meta:
        """
        Form Fields
        """

        model = SauceMethod
        fields = ("sauce_Steps",
                  )
        labels = {
            "sauce_Steps": "Steps",
        }
