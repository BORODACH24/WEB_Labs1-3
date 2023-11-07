from django.urls import path

from sandbox import views

urlpatterns = [
    path('', views.sandbox_view, name='sandbox_view'),
]
