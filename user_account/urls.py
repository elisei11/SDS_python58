from django.urls import path

from user_account import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Alte URL-uri existente
    path('account/edit/', views.edit_account, name='account_edit'),
    path('account/delete/', views.delete_account, name='account_delete'),
    path('account/', views.my_account, name='my_account'),
    path('password_reset/',views.change_password,name='password-reset'),

]

app_name = 'user_account'
