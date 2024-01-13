from django.contrib import admin
from .models import Sauce, SauceIngredients, SauceMethod


class SauceIndgredientsAdmin(admin.StackedInline):
    """
    Creates Admin For The Ingredients
    """
    model = SauceIngredients
    extra = 0


class SauceMethodAdmin(admin.StackedInline):
    """
    Creates Admin For The Method
    """
    model = SauceMethod
    extra = 0


class SauceRecipeAdmin(admin.ModelAdmin):
    """
    Creates Admin For The Main Part OF The Recipe And Adds Method
    And Ingredients To an Inline Output and Displays as one Item
    """
    fieldsets = []
    inlines = [SauceIndgredientsAdmin, SauceMethodAdmin]


admin.site.register(Sauce, SauceRecipeAdmin)
admin.site.register(SauceIngredients)
admin.site.register(SauceMethod)
