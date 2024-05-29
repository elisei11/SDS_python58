from django.contrib.auth.models import User
from django.urls import reverse_lazy

from django.views.generic import CreateView, ListView, TemplateView, DetailView

from .forms import CategoryForm, UserForm
from .models import Category, Product


class CategoryCreateView(CreateView):
    template_name = 'shop/create_category.html'
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy('list_categories')


class CategoryListView(ListView):
    template_name = 'shop/category_list.html'
    model = Category
    context_object_name = 'categories'

class HomeView(TemplateView):
    template_name = 'homepage.html'



class ListProductView(ListView):
    template_name = 'product/product_list.html'
    model = Product
    context_object_name = 'products'

class ProductDetailView(DetailView):
    template_name = 'product/product_detail.html'
    model = Product

class CreateCustomerView(CreateView):
    template_name = 'customer/create_customer.html'
    model = User
    form_class = UserForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        if form.is_valid():
            new_user = form.save(commit=False)

            # customizare first_name si last_name
            new_user.first_name = new_user.first_name.title()
            # atribui valoarea new_user.first_name.title() campului first_name al obiectului new_user
            new_user.last_name = new_user.last_name.title()
            new_user.save()




