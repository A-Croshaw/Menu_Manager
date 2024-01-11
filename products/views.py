from django.views.generic import (CreateView, ListView, DeleteView, UpdateView)
from .models import Product
from django.contrib.auth.mixins import (
    UserPassesTestMixin,
    LoginRequiredMixin
)

from .forms import ProductForm
from django.db.models import Q



class AddProduct(LoginRequiredMixin, CreateView):
    """Adding a Product"""

    template_name = "products/add_product.html"
    model = Product
    form_class = ProductForm
    success_url = "/products/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddProduct, self).form_valid(form)


class ProductList(ListView):
    """Product List"""

    template_name = "products/product.html"
    model = Product
    context_object_name = "products"

    def get_queryset(self, **kwargs):
        product_search = self.request.GET.get('q')
        if product_search:
            products = self.model.objects.filter(
                Q(product_name__icontains=product_search) |
                Q(product_type__icontains=product_search) |
                Q(product_freshness__icontains=product_search)
            )
        else:
            products = self.model.objects.all()
        return products


class DeleteProduct(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Delete Product"""
    model = Product
    success_url = '/products/'

    def test_func(self):
        return self.request.user == self.get_object().user



class EditProduct(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Edit a Product"""
    template_name = 'products/edit_product.html'
    model = Product
    form_class = ProductForm
    success_url = '/products/'

    def test_func(self):
        return self.request.user == self.get_object().user

