from django.shortcuts import render
from django.views import View
from shop.models.orders import Order
from rest_framework.response import Response
from rest_framework.decorators import api_view
from shop.models.orders import Order
from shop.serializers import OrderSerializer
from shop.serializers import OrderStatusUpdateSerializer
from rest_framework import status
from shop.serializers import ProductSerializer




class Orders(View):
    def get(self , request ):
        customer = request.session.get('customer')
        orders = Order.get_orders_by_customer(customer)
        return render(request , 'orders.html'  , {'orders' : orders})
@api_view(['GET'])
def get_all_orders(request):
    orders = Order.objects.all()
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def update_order_status(request):
    serializer = OrderStatusUpdateSerializer(data=request.data, many=True)
    
    if serializer.is_valid():
        for order_data in serializer.validated_data:
            try:
                order = Order.objects.get(order_id=order_data['order_id'])
                order.order_status = order_data['order_status']
                order.save()
            except Order.DoesNotExist:
                return Response({"error": f"Order with ID {order_data['order_id']} not found."}, status=status.HTTP_404_NOT_FOUND)
        
        return Response({"message": "Orders updated successfully."}, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def create_product(request):
    serializer = ProductSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)