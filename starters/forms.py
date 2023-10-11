from django import forms
from .models import Starter, StarterIngredients, StarterMethod


class StarterIngredientForm(forms.ModelForm):
    """
    Starter ingredient field form
    """
    class Meta:
        """
        Form Fields
        """
        model = StarterIngredients
        fields = (
                  'starter_ingredient',
                  'starter_quantity',
                  'starter_unit_type',
                  )
        labels = {
            'starter_ingredient': 'Ingredient',
            'starter_quantity': 'Quantity',
            'starter_unit_type': 'Unit',
        }


class StarterForm(forms.ModelForm):
    """
    Starter setup form
    """
    class Meta:
        """
        Form Fields
        """
        model = Starter
        fields = ("starter_name",
                  "starter_description",
                  "starter_type",
                  "starter_meat_type",)
        widget = {
            "starter_description": forms.Textarea(attrs={"rows": 5}),
        }
        labels = {
            "starter_name": "Name",
            "starter_description": "Description",
            "starter_type": "Type",
            "starter_meat_type": 'Meat type',
        }


class StarterMethodForm(forms.ModelForm):
    """
    Starter Method form
    """
    class Meta:
        """
        Form Fields
        """

        model = StarterMethod
        fields = ("starter_Steps",
                  )
        labels = {
            "starter_Steps": "Steps",
        }
