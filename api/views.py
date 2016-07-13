from location.models import Country, State, City
from rest_framework import viewsets
from .serializers import CountrySerializer, StateSerializer, CitySerializer

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.order_by("-created_time")
    serializer_class = CountrySerializer

class StateViewSet(viewsets.ModelViewSet):
    queryset = State.objects.order_by("-created_time")
    serializer_class = StateSerializer

class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.order_by("-created_time")
    serializer_class = CitySerializer
