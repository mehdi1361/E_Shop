from rest_framework import serializers
from location.models import Country, State, City
from products.models import Condition, Specification

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
