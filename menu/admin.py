from django.contrib import admin
from .models import Menu, StarterDishItem, MainDishItem, DessertDishItem, SideItem, SauceItem, Allegens


class StarterDishItemAdmin(admin.StackedInline):
    """
    Creates Admin For The Ingredients
    """
    model = StarterDishItem
    extra = 0


class MainDishItemAdmin(admin.StackedInline):
    """
    Creates Admin For The Method
    """
    model = MainDishItem
    extra = 0

class DessertDishItemAdmin(admin.StackedInline):
    """
    Creates Admin For The Ingredients
    """
    model = DessertDishItem
    extra = 0


class SideItemAdmin(admin.StackedInline):
    """
    Creates Admin For The Method
    """
    model = SideItem
    extra = 0


class SauceItemAdmin(admin.StackedInline):
    """
    Creates Admin For The Method
    """
    model = SauceItem
    extra = 0


class AllegensAdmin(admin.StackedInline):
    """
    Creates Admin For The Method
    """
    model = Allegens
    extra = 0


class MenuAdmin(admin.ModelAdmin):
    """
    Creates Admin For The Main Part OF The Recipe And Adds Method
    And Ingredients To an Inline Output and Displays as one Item
    """
    fieldsets = []
    inlines = [StarterDishItemAdmin, MainDishItemAdmin, DessertDishItemAdmin, SideItemAdmin, SauceItemAdmin, AllegensAdmin]


admin.site.register(Menu, MenuAdmin)
admin.site.register(StarterDishItem)
admin.site.register(MainDishItem)
admin.site.register(DessertDishItem)
admin.site.register(SideItem)
admin.site.register(SauceItem)
admin.site.register(Allegens)

