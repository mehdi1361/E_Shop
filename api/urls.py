from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'country', views.CountryViewSet)
router.register(r'state', views.StateViewSet)
router.register(r'city', views.CityViewSet)
router.register(r'condition', views.ConditionViewSet)
router.register(r'spec', views.SpecificationViewSet)

