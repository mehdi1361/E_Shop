from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'country', views.CountryViewSet)
router.register(r'state', views.StateViewSet)

