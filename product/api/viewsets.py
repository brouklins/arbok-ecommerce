from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import viewsets
from product.api import serializer
from product import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class  = serializer.ProductSerializer
    queryset = models.Product.objects.all()
    filter_backends = [DjangoFilterBackend]
    filter_backends = [filters.OrderingFilter]
    filterset_fields = ['name', 'brand', 'category', 'active']
    ordering_fields = ['price']
    

