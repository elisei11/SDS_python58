from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.views.decorators.http import require_http_methods

from django.views.generic import CreateView, ListView, TemplateView, DetailView, View, DeleteView, FormView

from .forms import UserForm, AddToCartForm, AddToFavoriteForm
from .models import Category, Product, CartItem, Cart, Subcategory, Favorite


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
        subcategories = Subcategory.objects.all()
        products = Product.objects.all()
        context = {
            'subcategories': subcategories,
            'products': products
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

    # def get_queryset(self):
    #     category_slug = self.kwargs.get('category_slug')
    #     queryset = Product.objects.all()
    #
    #     if category_slug:
    #         category = get_object_or_404(Category, slug=category_slug)
    #         queryset = queryset.filter(category=category)
    #
    #     return queryset
    #
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['categories'] = Category.objects.all()
    #     context['category'] = self.category
    #     return context


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
            return super().form_valid(form)


# class CartView(ListView):
#     model = CartItem
#     template_name = 'cart/view_cart.html'
#     context_object_name = 'carts'
#
#     def get_queryset(self):
#         cart, created = Cart.objects.get_or_create(user=self.request.user)
#         return CartItem.objects.filter(cart=cart)
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['cart'], created = Cart.objects.get_or_create(user=self.request.user)
#         for item in context['carts']:
#             item.total_price = item.product.price * item.quantity
#
#         total_price = sum(item.product.price * item.quantity for item in context['carts'])
#         context['total_price'] = total_price
#
#         return context
#
#
# class AddToCartView(FormView):
#     form_class = AddToCartForm
#     template_name = 'product/product_list.html'
#     success_url = reverse_lazy('shop:view_cart')
#
#     def get_form_kwargs(self):
#         kwargs = super().get_form_kwargs()
#         kwargs['initial'] = {'product_id': self.kwargs['pk']}
#         return kwargs
#
#     def form_valid(self, form):
#         product_id = form.cleaned_data['product_id']
#         quantity = form.cleaned_data['quantity']
#         product = get_object_or_404(Product, id=product_id)
#         cart, created = Cart.objects.get_or_create(user=self.request.user)
#         cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
#         if not created:
#             cart_item.quantity += quantity
#         else:
#             cart_item.quantity = quantity
#         cart_item.save()
#         return super().form_valid(form)
#
#
# class RemoveFromCartView(DeleteView):
#     template_name = 'cart/remove_from_cart.html'
#     model = CartItem
#     success_url = reverse_lazy('shop:view_cart')

# def get_queryset(self):
#     return self.model.objects.filter(user=self.request.user.id)


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


#
# #
# #
# #
# #
# # class AddToFavoriteView(FormView):
# #     form_class = AddToFavoriteForm
# #     template_name = 'favorite/view_favorite.html'
# #     success_url = reverse_lazy('shop:view_favorite')
# #
# #     def get_form_kwargs(self):
# #         kwargs = super().get_form_kwargs()
# #         kwargs['initial'] = {'product_id': self.kwargs['pk']}
# #         return kwargs
# #
# #     def form_valid(self, form):
# #         product_id = form.cleaned_data['product_id']
# #         product = get_object_or_404(Product, id=product_id)
# #         Favorite.objects.get_or_create(user=self.request.user, product=product)
# #         return super().form_valid(form)
# #
# #
class RemoveFromFavoriteView(DeleteView):
    template_name = 'favorite/remove_from_favorite.html'
    model = Favorite
    success_url = reverse_lazy('shop:view_favorite')

