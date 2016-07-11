from rest_framework import serializers
from location.models import Country, State

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ("id", "name", "slug", "description", "created_time")

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ("id", "name", "slug", "country", "description", "created_time")
        filter_fields = ('name', 'slug', 'country')
