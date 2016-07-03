from location.models import Country
from rest_framework import viewsets
from .serializers import CountrySerializer

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.order_by("-created_time")
    serializer_class = CountrySerializer

