from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import CreateView, ListView

from ecommerceproject.shop.forms import CategoryForm
from ecommerceproject.shop.models import Category


class CategoryCreateView(CreateView):
    template_name = 'shop/create_category.html'
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy('list_categories')


class CategoryListView(ListView):
    template_name = 'shop/category_list.html'
    model = Category
    context_object_name = 'categories'

