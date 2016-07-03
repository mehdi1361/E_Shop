from rest_framework import serializers
from location.models import Country

class ContrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ("id", "name", "slug", "description", "created_time")


