from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name = 'home'),
    path('orders/', views.get_orders, name = 'orders')
]