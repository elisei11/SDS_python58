from django.urls import path

from user_account import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Alte URL-uri existente
    path('account/edit/', views.edit_account, name='account_edit'),
    path('account/delete/', views.delete_account, name='account_delete'),
    path('account/orders/', views.order_history, name='order_history'),
    path('account/', views.my_account, name='my_account'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='user_account/password_reset.html'),
         name='password_reset'),
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='user_account/password_reset_done.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='user_account/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='user_account/password_reset_complete.html'),
         name='password_reset_complete'),
]

app_name = 'user_account'
