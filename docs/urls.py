from django.urls import path
from django.views.generic import TemplateView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions


schema_view = get_schema_view(
    openapi.Info(
        title="RealtorAgency.API",
        default_version='v1',
        description="",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    authentication_classes=[],
)


urlpatterns = [
    path('swagger-ui/', schema_view.with_ui('swagger',
                                            cache_timeout=0), name='schema-swagger-ui'),
]
