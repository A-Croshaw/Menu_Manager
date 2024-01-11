from django.urls import path
from .views import (
    AddProduct,
    DeleteProduct,
    ProductList,
    EditProduct
)


urlpatterns = [
    path("add/", AddProduct.as_view(), name="add_product"),
    path("", ProductList.as_view(), name="products"),
    path("delete/<slug:pk>/", DeleteProduct.as_view(), name="delete_product"),
    path("edit/<slug:pk>/", EditProduct.as_view(), name="edit_product",)

]
