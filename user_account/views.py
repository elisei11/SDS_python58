from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import EditAccountForm
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

