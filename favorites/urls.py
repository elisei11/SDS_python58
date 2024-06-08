from django.urls import path

from favorites import views

urlpatterns = [
    path('add_to_favorite/<int:product_id>/', views.add_to_favorites, name='add-to-favorite'),
    path('favorite/', views.view_favorites, name='view_favorite'),
    path('remove_from_favorite/<int:pk>/', views.remove_from_favorites, name='remove-from-favorite'),
]

app_name = 'favorites'
