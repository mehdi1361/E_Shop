from rest_framework import serializers
from location.models import Country, State, City
from products.models import Condition, Specification,SpecificationValue, Category, Product

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ("id", "name", "slug", "description", "created_time")

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ("id", "name", "slug", "country", "description", "created_time")
        filter_fields = ('name', 'slug', 'country')

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ("id", "name", "slug", "state", "description", "created_time")
        filter_fields = ('name', 'slug', 'state')

class ConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Condition
        fields = ("id", "created_time", "title", "slug")
        filter_fields = ('slug', 'title')

class SpecificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specification
        fields = ("id", "created_time", "title", "slug")
        filter_fields = ('slug', 'title')

class SpecificationValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecificationValue
        fields = ("id", "display_value", "is_filter_option", "slug", "created_time")
        filter_fields = ('slug', 'title')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name", "pub_date", "parent")
        filter_fields = ('id', 'name', 'parent')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "name", "pub_date", "parent", "is_hidden", "is_container", "priority_manual", "category")
        filter_fields = ('id', 'name', 'parent', 'is_hidden', 'is_container', 'priority_manual', 'category')
