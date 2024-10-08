from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import EditAccountForm, PasswordChange, UserForm
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
        return redirect('user_account:my_account')
    return render(request, 'user_account/delete_account.html')



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


class CreateCustomerView(CreateView):
    template_name = 'customer/create_customer.html'
    model = User
    form_class = UserForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        if form.is_valid():
            new_user = form.save(commit=False)

            # customizare first_name si last_name
            new_user.first_name = ''.join([char for char in new_user.first_name if char.isalpha()]).title()
            new_user.last_name = ''.join([char for char in new_user.last_name if char.isalpha()]).title()

            new_user.save()
            return super().form_valid(form)
