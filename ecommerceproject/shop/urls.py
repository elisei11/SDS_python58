from django.urls import path

from . import views

urlpatterns = [path('create_category/',views.CategoryCreateView.as_view(),name='create-category'),
               path('category_list/',views.CategoryListView.as_view(),name='category-list'),]

app_name = 'shop'