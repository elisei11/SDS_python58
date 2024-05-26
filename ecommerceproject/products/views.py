from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from .forms import ProductForm
from .models import Product



class CreateProductView(CreateView):
    template_name = 'product/create_product.html'
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('list_categories')


class ListProductView(ListView):
    template_name = 'product/list_products.html'
    model = Product
    context_object_name = 'products'

