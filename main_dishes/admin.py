from django.contrib import admin
from .models import MainDish, MainDishSauce, MainDishElement


class MainDishSauceAdmin(admin.StackedInline):
    """
    Creates Admin For The Ingredients
    """
    model = MainDishSauce
    extra = 0


class MainDishElementAdmin(admin.StackedInline):
    """
    Creates Admin For The Method
    """
    model = MainDishElement
    extra = 0


class MainDishesAdmin(admin.ModelAdmin):
    """
    Creates Admin For The Main Part OF The Recipe And Adds Method
    And Ingredients To an Inline Output and Displays as one Item
    """
    fieldsets = []
    inlines = [MainDishSauceAdmin, MainDishElementAdmin]


admin.site.register(MainDish, MainDishesAdmin)
admin.site.register(MainDishSauce)
admin.site.register(MainDishElement)

