from django import forms
from .models import Menu, StarterDishItem, MainDishItem, DessertDishItem, SideItem, Allegens


class StarterDishItemForm(forms.ModelForm):
    """
    Starter dish item field form
    """
    class Meta:
        """
        Form Fields
        """
        model = MainIngredients
        fields = (
            'menu',
            'starter_dish',
            'starter_price',
                  )
        labels = {
            'menu': 'Menu',
            'starter_dish': 'Starter Dish',
            'starter_price': 'Starter Price',
        }


class MainDishItemForm(forms.ModelForm):
    """
    Main dish item field form
    """
    class Meta:
        """
        Form Fields
        """
        model = MainIngredients
        fields = (
            'menu',
            'main_dish',
            'main_price',
                  )
        labels = {
            'menu': 'Menu',
            'main_dish': 'Main Dish',
            'main_price': 'Main Price',
        }


class DessertDishItemForm(forms.ModelForm):
    """
    Dessert dish item field form
    """
    class Meta:
        """
        Form Fields
        """
        model = MainIngredients
        fields = (
            'menu',
            'dessert_dish',
            'dessert_price',
                  )
        labels = {
            'menu': 'Menu',
            'dessert_dish': 'Dessert Dish',
            'dessert_price': 'Dessert Price',
        }


class SideItemForm(forms.ModelForm):
    """
    Side item field form
    """
    class Meta:
        """
        Form Fields
        """
        model = MainIngredients
        fields = (
            'menu',
            'side_dish',
            'side_price',
                  )
        labels = {
            'menu': 'Menu',
            'side_dish': 'Side Dish',
            'side_price': 'Side Price',
        }


class MenuForm(forms.ModelForm):
    """
    Menu field Form
    """
    class Meta:
        """
        Form Fields
        """
        model = Main
        fields = ("title",
                  "menu_date",
                  "date_updated",
                  "menu_type",
                  )
        widget = {
            "main_description": forms.Textarea(attrs={"rows": 5}),
        }
        labels = {
            "title": "Title",
            "menu_date": "Menu Date",
            "date_updated": "Date Updated",
            "menu_type": "Menu Type",
        }


class AllegensForm(forms.ModelForm):
    """
    Allegens form
    """
    class Meta:
        """
        Form Fields
        """

        model = MainMethod
        fields = ("allegens",
                  )
        labels = {
            "allegens": "Allegens",
        }
