from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import OrderSerializer
from .models import Order

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint':'/orders/',
            'method':'GET',
            'body':None,
            'description':'Returns an array of orders'
        },{
            'Endpoint':'/orders/id',
            'method':'GET',
            'body':None,
            'description':'Returns a single order object'
        },{
            'Endpoint':'/orders/create/',
            'method':'POST',
            'body':{'body':""},
            'description':'Creates an order with data sent in POST request'
        },{
            'Endpoint':'/orders/id/update/',
            'method':'PUT',
            'body':None,
            'description':'Recreates an existing order with updated data'
        },{
            'Endpoint':'/orders/id/delete/',
            'method':'DELETE',
            'body':None,
            'description':'Deletes an existing order'
        }
    ]
    return Response(routes)

@api_view(['GET',])
def get_orders(request):
    orders = Order.objects.all()
    serializer = OrderSerializer(orders, many = True)
    data = serializer.data
    return Response(data = data)

@api_view(['GET',])
def get_order(request, pk):
    orders = Order.objects.get(mobile = pk)
    serializer = OrderSerializer(orders, many = False)
    data = serializer.data
    return Response(data = data)

@api_view(['POST',])
def create_order(request):
    data = request.data
    order = Order.objects.create(**data)
    serializer = OrderSerializer(order, many = False)
    return Response(data = serializer.data)

@api_view(['PUT',])
def update_order(request, pk):
    order = Order.objects.get(mobile = pk)
    serializer = OrderSerializer(order, data = request.POST)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data) 

@api_view(['DELETE',])
def delete_order(request, pk):
    order = Order.objects.get(mobile = pk)
    order.delete()
    return Response("Order was Deleted", status = 204)

def render_order(request, pk):
    order = Order.objects.get(mobile = pk)
    return render(request, 'order.html', {'order':order})