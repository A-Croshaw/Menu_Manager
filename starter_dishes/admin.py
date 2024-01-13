from django.contrib import admin
from .models import StarterDish, StarterDishSauce, StarterDishElement


class StarterDishSauceAdmin(admin.StackedInline):
    """
    Creates Admin For The Ingredients
    """
    model = StarterDishSauce
    extra = 0


class StarterDishElementAdmin(admin.StackedInline):
    """
    Creates Admin For The Method
    """
    model = StarterDishElement
    extra = 0


class StarterDishesAdmin(admin.ModelAdmin):
    """
    Creates Admin For The Main Part OF The Recipe And Adds Method
    And Ingredients To an Inline Output and Displays as one Item
    """
    fieldsets = []
    inlines = [StarterDishSauceAdmin, StarterDishElementAdmin]


admin.site.register(StarterDish, StarterDishesAdmin)
admin.site.register(StarterDishSauce)
admin.site.register(StarterDishElement)
