from django.contrib import admin
from .models import Starter, StarterIngredients, StarterMethod


class StarterIndgredientsAdmin(admin.StackedInline):
    """
    Creates Admin For The Ingredients
    """
    model = StarterIngredients
    extra = 0


class StarterMethodAdmin(admin.StackedInline):
    """
    Creates Admin For The Method
    """
    model = StarterMethod
    extra = 0


class StarterRecipeAdmin(admin.ModelAdmin):
    """
    Creates Admin For The Main Part OF The Recipe And Adds Method
    And Ingredients To an Inline Output and Displays as one Item
    """
    fieldsets = []
    inlines = [StarterIndgredientsAdmin, StarterMethodAdmin]


admin.site.register(Starter, StarterRecipeAdmin)
admin.site.register(StarterIngredients)
admin.site.register(StarterMethod)
