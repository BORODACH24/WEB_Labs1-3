from django.urls import path
from . import views
from .views import LoginUser, RegisterUser

# from .views import LoginUser

urlpatterns = [
    path('', views.home_view, name='home'),
    path('privacy_policy/', views.privacy_policy_view, name='privacy_policy'),
    path('contacts/', views.contacts_view, name='contacts'),
    path('about_us/', views.about_us_view, name='about_us'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', RegisterUser.as_view(), name='signup'),

    path('hotels/<int:id>/', views.hotel_detail, name='hotel_detail'),
    path('hotels/', views.hotel_list, name='hotel_list'),
    path('hotels/search', views.search_hotels, name='search_hotels'),
    path('hotels/add', views.add_hotel, name='add_hotel'),
    path('hotels/', views.sort_hotels, name='sort_hotels'),
    path('hotels/delete/<int:id>/', views.delete_hotel, name='delete_hotel'),

    path('countries/<int:id>/', views.country_detail, name='country_detail'),
    path('countries/', views.country_list, name='country_list'),
    path('countries/search', views.search_countries, name='search_countries'),
    path('countries/add', views.add_country, name='add_country'),
    path('countries/', views.sort_countries, name='sort_countries'),
    path('countries/delete/<int:id>/', views.delete_country, name='delete_country'),

    path('tickets/<int:id>/', views.ticket_detail, name='ticket_detail'),
    path('tickets/', views.ticket_list, name='ticket_list'),
    path('tickets/search', views.search_tickets, name='search_tickets'),
    path('tickets/add', views.add_ticket, name='add_ticket'),
    path('tickets/', views.sort_tickets, name='sort_tickets'),
    path('tickets/delete/<int:id>/', views.delete_ticket, name='delete_ticket'),

    path('orders/<int:id>/', views.order_detail, name='order_detail'),
    path('orders/', views.order_list, name='order_list'),
    path('orders/add', views.add_order, name='add_order'),
    path('orders/delete/<int:id>/', views.delete_order, name='delete_order'),

    path('clients/<int:id>/', views.client_detail, name='client_detail'),
    path('clients/', views.client_list, name='client_list'),

    # re_path(r'^ticket/$', views.ticket_list, name='ticket_list'),
    # re_path(r'^ticket/$', views.ticket_detail, name='ticket_list'),

]
