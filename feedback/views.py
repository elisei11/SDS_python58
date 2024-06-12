from django.shortcuts import render, get_object_or_404

from feedback.forms import FeedbackForm
from feedback.models import Feedback
from shop.models import Product


def create_feedback(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.user = request.user
            feedback.product = product
            feedback.save()
        else:
            form = FeedbackForm(initial={'product': product})
        return render(request, 'feedback/create_feedback.html', {'form': form, 'product': product})


def view_feedback(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    feedbacks = Feedback.objects.filter(product=product)
    return render(request, 'feedback/view_feedback.html', {'feedbacks': feedbacks, 'product': product})
