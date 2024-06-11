from django.urls import path
from . import views

urlpatterns = [
    # alte căi URL
    path('search/', views.search_results, name='search_results'),
]
app_name = 'search'