from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import EditAccountForm, PasswordChange
from order.models import Order

@login_required
def my_account(request):
    return render(request, 'user_account/my_account.html')


@login_required
def edit_account(request):
    if request.method == 'POST':
        form = EditAccountForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('user_account:my_account')
    else:
        form = EditAccountForm(instance=request.user)
    return render(request, 'user_account/edit_account.html', {'form': form})

@login_required
def delete_account(request):
    if request.method == 'POST':
        request.user.delete()
        return redirect('user_account')
    return render(request, 'user_account/delete_account.html')

@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'user_account/order_history.html', {'orders': orders})


from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import PasswordChange  # Importă formularul tău personalizat

@login_required
def change_password(request):
    if request.method == 'POST':
        form_password = PasswordChange(user=request.user, data=request.POST)
        if form_password.is_valid():
            user = form_password.save()
            update_session_auth_hash(request, user)  # Important pentru a menține utilizatorul autentificat
            return redirect('user_account:my_account')
    else:
        form_password = PasswordChange(user=request.user)
    return render(request, 'user_account/change_password.html', {'form_password': form_password})
