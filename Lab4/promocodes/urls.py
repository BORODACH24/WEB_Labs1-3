from django.urls import path
from . import views

# from .views import LoginUser

urlpatterns = [
    path('', views.promo_codes_view, name='promo_codes'),
    path('delete/<int:id>/', views.delete_promo, name='delete_promo'),
    path('get/<int:id>/', views.get_promo, name='get_promo'),

    # path('<int:id>/', views.feedback_detail, name='feedback_detail'),
    # path('delete/<int:id>/', views.delete_feedback, name='delete_feedback'),
]
