from django import forms
from .models import StarterDish, StarterDishSauce, StarterDishElement


class StarterDishSauceForm(forms.ModelForm):
    """
    Starter Sauce Field Form
    """
    class Meta:
        """
        Form Fields
        """
        model = StarterDishSauce
        fields = (
                  'starter_dish_sauce',
                  )
        labels = {
            'starter_dish_sauce': 'Sauce',
        }


class StarterDishForm(forms.ModelForm):
    """
    Starter Dish Form
    """
    class Meta:
        """
        Form Fields
        """
        model = StarterDish
        fields = ("starter_dish_name",
                  "starter_dish_description",
                  "starter_dish_type",
                  )
        widget = {
            "starter_dish_description": forms.Textarea(attrs={"rows": 5}),
        }
        labels = {
            "starter_dish_name": "Name",
            "starter_dish_description": "Description",
            "starter_dish_type": "Type",
        }


class StarterDishElementForm(forms.ModelForm):
    """
    Starter Element form
    """
    class Meta:
        """
        Form Fields
        """

        model = StarterDishElement
        fields = ("starter_dish_element",
                  )
        labels = {
            "starter_dish_element": "Element",
        }
