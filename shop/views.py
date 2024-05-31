from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy

from django.views.generic import CreateView, ListView, TemplateView, DetailView, View

from .forms import CategoryForm, UserForm
from .models import Category, Product, CartItem, Cart


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

    def product_list(request, category_slug=None):
        category = None
        categories = Category.objects.all()
        products = Product.objects.all()

        if category_slug:
            category = get_object_or_404(Category, slug=category_slug)
            products = products.filter(category=category)

        return render(request, 'product/product_list.html', {
            'category': category,
            'categories': categories,
            'products': products
        })

    # def get_queryset(self):
    #     return Category.objects.filter(product__slug=self.kwargs['slug'])


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


class CartView(ListView):
    model = CartItem
    template_name = 'cart/view_cart.html'

    def get_queryset(self):
        cart, created = Cart.objects.get_or_create(user=self.request.user)
        return CartItem.objects.filter(cart=cart)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart'], created = Cart.objects.get_or_create(user=self.request.user)
        return context


class AddToCartView(View):

    def post(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        if not created:
            cart_item.quantity += 1
            cart_item.save()
        return redirect('view_cart')


class RemoveFromCartView(View):

    def post(self, request, item_id):
        cart_item = get_object_or_404(CartItem, id=item_id)
        cart_item.delete()
        return redirect('view_cart')
