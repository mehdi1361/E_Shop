from location.models import Country, State, City
from products.models import Condition, Specification
from rest_framework import viewsets
from .serializers import CountrySerializer, StateSerializer, CitySerializer, ConditionSerializer, SpecificationSerializer
# from rest_frameworkssct import  django_filters
class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.order_by("-created_time")
    serializer_class = CountrySerializer
    filter_fields = ('name', 'slug', 'country')

class StateViewSet(viewsets.ModelViewSet):
    queryset = State.objects.order_by("-created_time")
    serializer_class = StateSerializer

class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.order_by("-created_time")
    serializer_class = CitySerializer

class ConditionViewSet(viewsets.ModelViewSet):
    queryset = Condition.objects.order_by("-created_time")
    serializer_class = ConditionSerializer

class SpecificationViewSet(viewsets.ModelViewSet):
    queryset = Specification.objects.order_by("-created_time")
    serializer_class = SpecificationSerializer
