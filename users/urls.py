from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import UserViewSet

router = DefaultRouter()

router.register('user', UserViewSet, 'user')

urlpatterns = [
    path(r'', include(router.urls))
]
