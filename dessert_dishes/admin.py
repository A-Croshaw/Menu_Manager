from django.contrib import admin
from .models import DessertDish, DessertDishSauce, DessertDishElement


class DessertDishSauceAdmin(admin.StackedInline):
    """
    Creates Admin For The Ingredients
    """
    model = DessertDishSauce
    extra = 0


class DessertDishElementAdmin(admin.StackedInline):
    """
    Creates Admin For The Method
    """
    model = DessertDishElement
    extra = 0


class DessertDishesAdmin(admin.ModelAdmin):
    """
    Creates Admin For The Main Part OF The Recipe And Adds Method
    And Ingredients To an Inline Output and Displays as one Item
    """
    fieldsets = []
    inlines = [DessertDishSauceAdmin, DessertDishElementAdmin]


admin.site.register(DessertDish, DessertDishesAdmin)
admin.site.register(DessertDishSauce)
admin.site.register(DessertDishElement)

