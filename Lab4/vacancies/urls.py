from django.urls import path
from . import views

# from .views import LoginUser

urlpatterns = [
    path('', views.vacancies_list, name='vacancies_list'),
    path('<int:id>/', views.vacancy_detail, name='vacancy_detail'),
    path('delete/<int:id>/', views.delete_vacancy, name='delete_vacancy'),
]
