from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import RealtyViewSet, ClientViewSet

router = DefaultRouter()

router.register('realty', RealtyViewSet, 'realty')
router.register('client', ClientViewSet, 'client')

urlpatterns = [
    path(r'', include(router.urls))
]
