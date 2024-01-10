from django import forms
from .models import Menu, StarterDishItem, MainDishItem, DessertDishItem, SideItem, SauceItem


class StarterDishItemForm(forms.ModelForm):
    """
    Starter dish item field form
    """
    class Meta:
        """
        Form Fields
        """
        model = StarterDishItem
        fields = (
            'starter_dish',
            'starter_price',
                  )
        labels = {
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
        model = MainDishItem
        fields = (
            'main_dish',
            'main_price',
                  )
        labels = {
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
        model = DessertDishItem
        fields = (
            'dessert_dish',
            'dessert_price',
                  )
        labels = {
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
        model = SideItem
        fields = (
            'side',
            'side_price',
                  )
        labels = {
            'side': 'Side',
            'side_price': 'Side Price',
        }


class SauceItemForm(forms.ModelForm):
    """
    Sauce item field form
    """
    class Meta:
        """
        Form Fields
        """
        model = SauceItem
        fields = (
            'sauce',
            'sauce_price',
                  )
        labels = {
            'sauce': 'Sauce',
            'sacue_price': 'Sauce Price',
        }


class MenuForm(forms.ModelForm):
    """
    Menu field Form
    """
    class Meta:
        """
        Form Fields
        """
        model = Menu
        fields = ("title",
                  "menu_type",
                  )
        labels = {
            "title": "Menu Title",
            "menu_type": "Menu Type",
        }

