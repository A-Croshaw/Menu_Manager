from django import forms
from .models import Main, MainIngredients, MainMethod


class MainIngredientForm(forms.ModelForm):
    """
    main ingredient field form
    """
    class Meta:
        """
        Form Fields
        """
        model = MainIngredients
        fields = (
                  'main_ingredient',
                  'main_quantity',
                  'main_unit_type',
                  )
        labels = {
            'main_ingredient': 'Ingredient',
            'main_quantity': 'Quantity',
            'main_unit_type': 'Unit',
        }


class MainForm(forms.ModelForm):
    """
    main setup form
    """
    class Meta:
        """
        Form Fields
        """
        model = Main
        fields = ("main_name",
                  "main_description",
                  "main_type",
                  "main_meat_type",)
        widget = {
            "main_description": forms.Textarea(attrs={"rows": 5}),
        }
        labels = {
            "main_name": "Name",
            "main_description": "Description",
            "main_type": "Type",
            "main_meat_type": 'Meat type',
        }


class MainMethodForm(forms.ModelForm):
    """
    main Method form
    """
    class Meta:
        """
        Form Fields
        """

        model = MainMethod
        fields = ("main_Steps",
                  )
        labels = {
            "main_Steps": "Steps",
        }
