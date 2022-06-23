from .models import Order, Item
from rest_framework import serializers
from rest_framework.fields import ListField, CharField, FloatField



class ItemSerializer(serializers.Serializer):
    """customized serializer for Item Model

    Args:
        serializers (_type_): _description_

    Returns:
        # object instance like below which 
        # confirms to the ITEM Model
        {
            "item_name": "earphone",
            "item_quantity": 2.0,
            "item_price": 995.5
        } 
    """
    item_name = CharField(max_length = 140)
    item_quantity = FloatField()
    item_price = FloatField()

    def create(self, validated_data):
        return Item(**validated_data)

    def update(self, instance, validated_data):
        instance.item_name = validated_data.get('item_name', instance.item_name)
        instance.item_quantity = validated_data.get('item_quantity', instance.item_quantity)
        instance.item_price = validated_data.get('item_price', instance.item_price)
        
        return instance


class OrderSerializer(serializers.ModelSerializer):
    
    # the child serializer has been passed to parse the 
    # stored dictionaries inside the list so that it 
    # can also be represented as JSON field insted of a 
    # joined string of all objects 
    
    items = ListField(child = ItemSerializer())
    
    class Meta:
        model = Order 
        # Model is a class Model for which we 
        # want serialized data to conform to
        fields = "__all__"