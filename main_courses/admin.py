from django.contrib import admin
from .models import Main, MainIngredients, MainMethod


class MainIndgredientsAdmin(admin.StackedInline):
    """
    Creates Admin For The Ingredients
    """
    model = MainIngredients
    extra = 0


class MainMethodAdmin(admin.StackedInline):
    """
    Creates Admin For The Method
    """
    model = MainMethod
    extra = 0


class MainRecipeAdmin(admin.ModelAdmin):
    """
    Creates Admin For The Main Part OF The Recipe And Adds Method
    And Ingredients To an Inline Output and Displays as one Item
    """
    fieldsets = []
    inlines = [MainIndgredientsAdmin, MainMethodAdmin]


admin.site.register(Main, MainRecipeAdmin)
admin.site.register(MainIngredients)
admin.site.register(MainMethod)
