from django.contrib import admin
from .models import DessertSauce, DessertSauceIngredients, DessertSauceMethod


class DessertSauceIndgredientsAdmin(admin.StackedInline):
    """
    Creates Admin For The Ingredients
    """
    model = DessertSauceIngredients
    extra = 0


class DessertSauceMethodAdmin(admin.StackedInline):
    """
    Creates Admin For The Method
    """
    model = DessertSauceMethod
    extra = 0


class DessertSauceRecipeAdmin(admin.ModelAdmin):
    """
    Creates Admin For The Main Part OF The Recipe And Adds Method
    And Ingredients To an Inline Output and Displays as one Item
    """
    fieldsets = []
    inlines = [DessertSauceIndgredientsAdmin, DessertSauceMethodAdmin]


admin.site.register(DessertSauce, DessertSauceRecipeAdmin)
admin.site.register(DessertSauceIngredients)
admin.site.register(DessertSauceMethod)
