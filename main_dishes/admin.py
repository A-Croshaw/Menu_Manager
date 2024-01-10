from django.contrib import admin
from .models import MainDish, MainDishSauce, MainDishElement, MainDishSide


class MainDishSauceAdmin(admin.StackedInline):
    """
    Creates Admin For The Dish Sauces
    """
    model = MainDishSauce
    extra = 0


class MainDishElementAdmin(admin.StackedInline):
    """
    Creates Admin For The Dish Elements
    """
    model = MainDishElement
    extra = 0


class MainDishSideAdmin(admin.StackedInline):
    """
    Creates Admin For The Dish Sides
    """
    model = MainDishSide
    extra = 0


class MainDisheAdmin(admin.ModelAdmin):
    """
    Creates Admin For The Main Part OF The Dish  And Adds Sauces, Elements
    And Sides To an Inline Output and Displays as one Item
    """
    fieldsets = []
    inlines = [MainDishSauceAdmin, MainDishElementAdmin, MainDishSideAdmin]


admin.site.register(MainDish, MainDisheAdmin)
admin.site.register(MainDishSauce)
admin.site.register(MainDishElement)
admin.site.register(MainDishSide)
