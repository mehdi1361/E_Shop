from location.models import Country, State
from rest_framework import viewsets
from .serializers import CountrySerializer, StateSerializer

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.order_by("-created_time")
    serializer_class = CountrySerializer

class StateViewSet(viewsets.ModelViewSet):
    queryset = State.objects.order_by("-created_time")
    serializer_class = StateSerializer
