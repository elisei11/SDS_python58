from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.views.decorators.http import require_http_methods

from django.views.generic import CreateView, ListView, TemplateView, DetailView, View, DeleteView

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


class HomeView(ListView):
    template_name = 'homepage.html'
    model = Product
    context_object_name = 'products'



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
    context_object_name = 'carts'

    def get_queryset(self):
        cart, created = Cart.objects.get_or_create(user=self.request.user)
        return CartItem.objects.filter(cart=cart)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart'], created = Cart.objects.get_or_create(user=self.request.user)
        return context


class AddToCartView(View):

    def post(self, request, pk):
        cart = request.session.get('cart', {})
        if pk in cart:
            cart[pk] += 1  # Crește cantitatea dacă produsul este deja în coș
        else:
            cart[pk] = 1  # Adaugă produsul nou în coș cu cantitatea 1

        request.session['cart'] = cart  # Salvează coșul în sesiune

        response = {
            'status': 'success',
            'item_id': pk,
            'quantity': cart[pk]
        }
        return JsonResponse(response)

    def get(self, request, pk):
        # Returnează un mesaj de succes în cazul unei cereri GET
        response = {
            'status': 'success',
            'message': 'GET method allowed'
        }
        return JsonResponse(response)

class RemoveFromCartView(View):
    @require_http_methods(["GET", "POST"])
    def post(self,request, pk):
        if request.method == "POST":
            cart = request.session.get('cart', {})
            if pk in cart:
                del cart[pk]  # Elimină produsul din coș
                request.session['cart'] = cart  # Salvează coșul actualizat în sesiune

                return JsonResponse({'status': 'success'})
            else:
                return JsonResponse({'status': 'error', 'message': 'Item not found in cart'}, status=404)
        else:
            # Returnează un mesaj de succes în cazul unei cereri GET
            response = {
                'status': 'success',
                'message': 'GET method allowed'
            }
            return JsonResponse(response)