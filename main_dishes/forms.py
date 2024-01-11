from django import forms
from .models import MainDish, MainDishSauce, MainDishElement, MainDishSide


class MainDishSauceForm(forms.ModelForm):
    """
    Main Sauce Field Form
    """
    class Meta:
        """
        Form Fields
        """
        model = MainDishSauce
        fields = (
                  'main_dish_sauce',
                  )
        labels = {
            'main_dish_sauce': 'Sauce',
        }


class MainDishForm(forms.ModelForm):
    """
    Main Dish Form
    """
    class Meta:
        """
        Form Fields
        """
        model = MainDish
        fields = ("main_dish_name",
                  "main_dish_description",
                  "main_dish_type",
                  )
        widget = {
            "main_dish_description": forms.Textarea(attrs={"rows": 5}),
        }
        labels = {
            "main_dish_name": "Name",
            "main_dish_description": "Description",
            "main_dish_type": "Type",
        }


class MainDishElementForm(forms.ModelForm):
    """
    main Element form
    """
    class Meta:
        """
        Form Fields
        """

        model = MainDishElement
        fields = ("main_dish_element",
                  )
        labels = {
            "main_dish_element": "Element",
        }


class MainDishSideForm(forms.ModelForm):
    """
    main side form
    """
    class Meta:
        """
        Form Fields
        """

        model = MainDishSide
        fields = ("main_dish_side",
                  )
        labels = {
            "main_dish_side": "Side",
        }
