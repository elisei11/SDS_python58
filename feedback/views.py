from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy

from feedback.forms import FeedbackForm
from feedback.models import Feedback
from shop.models import Product


#
# def create_feedback(request, product_id):
#     product = get_object_or_404(Product, id=product_id)
#     if request.method == 'POST':
#         form = FeedbackForm(request.POST)
#         if form.is_valid():
#             feedback = form.save(commit=False)
#             feedback.user = request.user
#             feedback.product = product
#             feedback.save()
#         else:
#             form = FeedbackForm(initial={'product': product})
#         return render(request, 'feedback/create_feedback.html', {'form': form, 'product': product})
# class CreateFeedbackView(CreateView):
#     template_name = 'feedback/create_feedback.html'
#     model = Feedback
#     form_class = FeedbackForm
#     success_url = reverse_lazy('home')
@login_required
def create_feedback(request, product_id):
    product = get_object_or_404(Product, pk=product_id)  # Retrieve the product instance
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.user = request.user  # Ensure the user is set
            feedback.product = product  # Associate feedback with the product
            feedback.save()
            return redirect('feedback:view-feedback', product_id=product.id)  # Redirect to the product's feedback view
    else:
        form = FeedbackForm()
    return render(request, 'feedback/create_feedback.html', {'form': form, 'product': product})


def view_feedback(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    feedbacks = Feedback.objects.filter(product=product)
    return render(request, 'feedback/view_feedback.html', {'feedbacks': feedbacks, 'product': product})
