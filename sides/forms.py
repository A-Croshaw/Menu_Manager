from django import forms
from .models import Side, SideIngredients, SideMethod


class SideIngredientForm(forms.ModelForm):
    """
    Side ingredient field form
    """
    class Meta:
        """
        Form Fields
        """
        model = SideIngredients
        fields = (
                  'side_ingredient',
                  'side_quantity',
                  'side_unit_type',
                  )
        labels = {
            'side_ingredient': 'Ingredient',
            'side_quantity': 'Quantity',
            'side_unit_type': 'Unit',
        }


class SideForm(forms.ModelForm):
    """
    Side setup form
    """
    class Meta:
        """
        Form Fields
        """
        model = Side
        fields = ("side_name",
                  "side_description",
                  "side_type",)
        widget = {
            "side_description": forms.Textarea(attrs={"rows": 5}),
        }
        labels = {
            "side_name": "Name",
            "side_description": "Description",
            "side_type": "Type",
        }


class SideMethodForm(forms.ModelForm):
    """
    Side Method form
    """
    class Meta:
        """
        Form Fields
        """

        model = SideMethod
        fields = ("side_Steps",
                  )
        labels = {
            "side_Steps": "Steps",
        }
