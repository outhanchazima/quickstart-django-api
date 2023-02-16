from django.conf import settings
from drf_yasg import openapi
from drf_yasg.generators import OpenAPISchemaGenerator
from drf_yasg.views import get_schema_view
from rest_framework import permissions


class CustomOpenAPISchemaGeneratorSandbox(OpenAPISchemaGenerator):
    def get_schema(self, request=None, public=False):
        schema = super().get_schema(request, public)
        schema.base_path = '/quicksta-api/'
        return schema


class CustomOpenAPISchemaGeneratorProd(OpenAPISchemaGenerator):
    def get_schema(self, request=None, public=False):
        schema = super().get_schema(request, public)
        schema.base_path = '/api/'
        return schema


if settings.MODE == 'DEV':
    GENERATOR_CLASS = None
if settings.MODE == 'SANDBOX' or settings.MODE == 'CI':
    GENERATOR_CLASS = CustomOpenAPISchemaGeneratorSandbox
if settings.MODE == 'PROD':
    GENERATOR_CLASS = CustomOpenAPISchemaGeneratorProd


schema_view = get_schema_view(
   urlconf='QuickStartAPI.urls',
   info=openapi.Info(
      title="QuickStartAPI",
      default_version='v1',
      description="QuickStartAPI",
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
   generator_class=GENERATOR_CLASS,
)
