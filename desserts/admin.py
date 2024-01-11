from django.contrib import admin
from .models import Dessert, DessertIngredients, DessertMethod


class DessertIndgredientsAdmin(admin.StackedInline):
    """Creates Admin For The Ingredients"""

    model = DessertIngredients
    extra = 0


class DessertMethodAdmin(admin.StackedInline):
    """Creates Admin For The Method"""

    model = DessertMethod
    extra = 0


class DessertRecipeAdmin(admin.ModelAdmin):
    """Creates Admin For The Main Part OF The Recipe And Adds Method
    And Ingredients To an Inline Output and Displays as one Item"""
    
    fieldsets = []
    inlines = [DessertIndgredientsAdmin, DessertMethodAdmin]


admin.site.register(Dessert, DessertRecipeAdmin)
admin.site.register(DessertIngredients)
admin.site.register(DessertMethod)
