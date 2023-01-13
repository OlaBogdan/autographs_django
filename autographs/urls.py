from django.urls import include, path
from rest_framework import routers

from .api import PersonViewSet, AddressViewSet, LetterViewSet

router = routers.DefaultRouter()
router.register(r'people', PersonViewSet)
router.register(r'addresses', AddressViewSet)
router.register(r'letters', LetterViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
