from django.urls import path

from feedback import views
from feedback.views import view_feedback, create_feedback

urlpatterns = [
    path('create_feedback/<int:product_id>/', create_feedback, name='create-feedback'),
    path('view/<int:product_id>/', view_feedback, name='view-feedback'),
]

app_name = 'feedback'
