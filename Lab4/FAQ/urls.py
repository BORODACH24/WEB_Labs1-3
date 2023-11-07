from django.urls import path
from . import views

# from .views import LoginUser

urlpatterns = [
    path('', views.FAQ_list, name='FAQ_list'),
    path('<int:id>/', views.FAQ_detail, name='FAQ_detail'),
    path('add', views.add_FAQ, name='add_FAQ'),
    path('', views.sort_FAQ, name='sort_FAQ'),
    path('delete/<int:id>/', views.delete_FAQ, name='delete_FAQ'),
]
