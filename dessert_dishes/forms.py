from django import forms
from .models import DessertDish, DessertDishSauce, DessertDishElement


class DessertDishSauceForm(forms.ModelForm):
    """
    Dessert Sauce Field Form
    """
    class Meta:
        """
        Form Fields
        """
        model = DessertDishSauce
        fields = (
                  'dessert_dish_sauce',
                  )
        labels = {
            'dessert_dish_sauce': 'Sauce',
        }


class DessertDishForm(forms.ModelForm):
    """
    Dessert Dish Form
    """
    class Meta:
        """
        Form Fields
        """
        model = DessertDish
        fields = ("dessert_dish_name",
                  "dessert_dish_description",
                  "dessert_dish_type",
                  )
        widget = {
            "dessert_dish_description": forms.Textarea(attrs={"rows": 5}),
        }
        labels = {
            "dessert_dish_name": "Name",
            "dessert_dish_description": "Description",
            "dessert_dish_type": "Type",
        }


class DessertDishElementForm(forms.ModelForm):
    """
    Dessert Element form
    """
    class Meta:
        """
        Form Fields
        """

        model = DessertDishElement
        fields = ("dessert_dish_element",
                  )
        labels = {
            "dessert_dish_element": "Element",
        }
