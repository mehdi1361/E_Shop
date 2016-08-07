from location.models import Country, State, City
from products.models import Condition, Specification, SpecificationValue, Category, Product
from rest_framework import viewsets
from .serializers import *


class DefaultsMixin(object):
     """Default settings for view authentication, permissions,filtering and pagination."""
     # authentication_classes = 
     # (
             # authentication.BasicAuthentication,
             # authentication.TokenAuthentication,
     # )

     # permission_classes = (
             # permissions.IsAuthenticated, 
     # )

     paginate_by = 10

     max_paginate_by = 100 
# from rest_frameworkssct import  django_filters

class CountryViewSet(DefaultsMixin,viewsets.ModelViewSet):
    queryset = Country.objects.order_by("-created_time")
    serializer_class = CountrySerializer
    filter_fields = ('name', 'slug', 'country')

class StateViewSet(viewsets.ModelViewSet):
    queryset = State.objects.order_by("-created_time")
    serializer_class = StateSerializer
    filter_fields = ('name', 'slug', 'state')

class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.order_by("-created_time")
    serializer_class = CitySerializer
    filter_fields = ('name', 'slug')

class ConditionViewSet(viewsets.ModelViewSet):
    queryset = Condition.objects.order_by("-created_time")
    serializer_class = ConditionSerializer
    filter_fields = ('title', 'slug')

class SpecificationViewSet(viewsets.ModelViewSet):
    queryset = Specification.objects.order_by("-created_time")
    serializer_class = SpecificationSerializer
    filter_fields = ('created_time', 'slug', 'title', 'spec_type')

class SpecificationValueViewSet(viewsets.ModelViewSet):
    queryset = SpecificationValue.objects.order_by("-created_time")
    serializer_class = SpecificationValueSerializer
    filter_fields = ('created_time', 'slug', 'display_value', 'specification')

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.order_by("id")
    serializer_class = CategorySerializer
    filter_fields = ('id', 'name', 'pub_date', 'parent')

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.order_by("id")
    serializer_class = ProductSerializer
    filter_fields = ('id', 'name', 'pub_date', 'parent', 'is_hidden', 'is_container', 'priority_manual', 'category')

