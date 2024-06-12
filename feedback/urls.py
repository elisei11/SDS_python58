from django.urls import path

from feedback.views import create_feedback, view_feedback

urlpatterns = [
    path('create/<int:product_id>/', create_feedback, name='create_feedback'),
    path('view/<int:product_id>/', view_feedback, name='view_feedback'),
]

app_name = 'feedback'
