from django.urls import path
from . import views

urlpatterns = [
    # alte căi URL
    path('<str:query_string>', views.search_results, name='search_results'),
]
app_name = 'search'