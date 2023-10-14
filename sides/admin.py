from django.contrib import admin
from .models import Side, SideIngredients, SideMethod


class SideIndgredientsAdmin(admin.StackedInline):
    """
    Creates Admin For The Ingredients
    """
    model = SideIngredients
    extra = 0


class SideMethodAdmin(admin.StackedInline):
    """
    Creates Admin For The Method
    """
    model = SideMethod
    extra = 0


class SideRecipeAdmin(admin.ModelAdmin):
    """
    Creates Admin For The Main Part OF The Recipe And Adds Method
    And Ingredients To an Inline Output and Displays as one Item
    """
    fieldsets = []
    inlines = [SideIndgredientsAdmin, SideMethodAdmin]


admin.site.register(Side, SideRecipeAdmin)
admin.site.register(SideIngredients)
admin.site.register(SideMethod)
