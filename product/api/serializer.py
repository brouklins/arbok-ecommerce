from rest_framework import serializers
from product import models

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = [
            '_id',
            'name',
            'category',
            'brand',
            'description',
            'stock',
            'active',
            'rating',
            'price',
            'create_at'
        ]
        

