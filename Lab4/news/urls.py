from django.urls import path
from . import views

# from .views import LoginUser

urlpatterns = [
    path('', views.news_list, name='news_list'),
    path('<int:id>/', views.news_detail, name='news_detail'),
    path('search', views.news_hotels, name='search_news'),
    path('add', views.add_news, name='add_news'),
    path('', views.sort_news, name='sort_news'),
    path('delete/<int:id>/', views.delete_news, name='delete_news'),
]
