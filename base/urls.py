from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name = 'home'),
    path('orders/', views.get_orders, name = 'orders'),
    path("orders/create/", views.create_order, name="create order"),
    path("orders/<str:pk>/update", views.create_order, name="update order"),
    path("orders/<str:pk>/delete", views.delete_order, name="delete order"),
    path('orders/<str:pk>/', views.get_order, name = 'order'),   
    path('orders/<str:pk>/htm', views.render_order, name = 'render order'),
]