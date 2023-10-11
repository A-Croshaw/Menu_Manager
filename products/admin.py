from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "product_name",
        "product_type",
        "product_freshness",
        "product_cost",
        "product_quantity",
    )
    list_filter = ("product_type", "product_freshness",)
    ordering = ('product_type', 'product_name', 'product_freshness',)
