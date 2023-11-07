from django.urls import path
from . import views

# from .views import LoginUser

urlpatterns = [
    path('', views.feedback_list, name='feedback_list'),
    path('<int:id>/', views.feedback_detail, name='feedback_detail'),
    path('delete/<int:id>/', views.delete_feedback, name='delete_feedback'),
]
