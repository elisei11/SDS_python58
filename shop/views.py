from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, DeleteView

from cart.forms import AddToCartForm
from cart.models import CartItem, Cart
from favorites.forms import AddToFavoriteForm
from .models import Category, Product, Subcategory


class CategoryListView(ListView):
    template_name = 'shop/category_list.html'
    model = Category
    context_object_name = 'categories'


class HomeView(ListView):
    template_name = 'homepage.html'
    model = Product
    context_object_name = 'products'
    add_to_cart_form = AddToCartForm
    favorite_form = AddToFavoriteForm

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['favorite_product_form'] = self.favorite_form
        context['add_to_cart_form'] = self.add_to_cart_form
        return context

    def get(self, request, *args, **kwargs):
        relevant_categories = ["Tricouri", "Shoes", "Tools"]
        subcategories = Subcategory.objects.filter(name__in=relevant_categories)
        products = Product.objects.all()
        featured_products = Product.objects.filter(favorite=True)
        context = {
            'subcategories': subcategories,
            'products': products,
            'featured_products': featured_products,
        }
        return render(request, 'homepage.html', context)


class ListProductView(ListView):
    template_name = 'product/product_list.html'
    context_object_name = 'products'
    category = None

    def get_queryset(self):
        subcategory_slug = self.kwargs.get('subcategory_slug')
        subcategory = get_object_or_404(Subcategory, slug=subcategory_slug)
        return Product.objects.filter(subcategory=subcategory)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        subcategory_slug = self.kwargs.get('subcategory_slug')
        subcategory = get_object_or_404(Subcategory, slug=subcategory_slug)
        context['subcategory'] = subcategory
        context['category'] = subcategory.category  # Adăugăm și categoria părinte pentru context
        return context


class ProductDetailView(DetailView):
    template_name = 'product/product_detail.html'
    model = Product
    context_object_name = 'product'

    def post(self, request, *args, **kwargs):
        form = AddToCartForm(request.POST)
        if form.is_valid():
            product_id = form.cleaned_data['product_id']
            quantity = form.cleaned_data['quantity']
            product = get_object_or_404(Product, id=product_id)
            cart, created = Cart.objects.get_or_create(user=request.user)
            cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
            if not created:
                cart_item.quantity += quantity
            else:
                cart_item.quantity = quantity
            cart_item.save()
            return redirect('shop:view_cart')
        return self.get(request, *args, **kwargs)




#

class SubCategoryListView(ListView):
    model = Subcategory
    template_name = 'subcategory/subcategory_list.html'
    context_object_name = 'subcategories'

    def get_queryset(self):
        category_slug = self.kwargs.get('category_slug')
        category = get_object_or_404(Category, slug=category_slug)
        return Subcategory.objects.filter(category=category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_slug = self.kwargs.get('category_slug')
        category = get_object_or_404(Category, slug=category_slug)
        context['category'] = category
        return context



