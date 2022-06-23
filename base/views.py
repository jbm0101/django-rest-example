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
def get_orders(request, pk):
    orders = Order.objects.get(id = pk)
    serializer = OrderSerializer(orders, many = False)
    data = serializer.data
    return Response(data = data)