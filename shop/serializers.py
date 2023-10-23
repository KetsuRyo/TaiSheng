from rest_framework import serializers
from .models.orders import Order
from .models.products import Product
from .models.customers import Customer


class CustomerNameField(serializers.RelatedField):
    def to_representation(self, value):
        return f"{value.fname} {value.lname}"
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'price', 'category', 'description', 'image']
class OrderSerializer(serializers.ModelSerializer):
    customer = CustomerNameField(queryset=Customer.objects.all())
    class Meta:
        model = Order
        fields = ['product', 'customer', 'quantity', 'price', 'address', 'phone', 'order_id', 'order_date', 'order_status']
class OrderStatusUpdateSerializer(serializers.Serializer):
    order_id = serializers.CharField(max_length=50)
    order_status = serializers.BooleanField()