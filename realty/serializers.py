from rest_framework import serializers, exceptions
from drf_extra_fields.relations import PresentablePrimaryKeyRelatedField

from .models import Realty, RealtyImage, Client, Category


# region Realty


class RealtyListSerializer(serializers.ModelSerializer):
    client = serializers.StringRelatedField()

    class Meta:
        model = Realty
        fields = ('id', 'title', 'client')


class RealtyImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RealtyImage
        fields = ('id', 'image')


class RealtySerializer(serializers.ModelSerializer):
    realty_images = RealtyImageSerializer(
        many=True, read_only=True)

    class Meta:
        model = Realty
        fields = '__all__'
        read_only = ('created_by',)
        extra_kwargs = {
            'client': {'required': True}
        }

# endregion

# region Client


class ClientListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'email', 'full_name')


class ClientSerializer(serializers.ModelSerializer):
    realties = PresentablePrimaryKeyRelatedField(
        presentation_serializer=RealtyListSerializer,
        queryset=Realty.objects.all(),
        many=True,
        allow_null=True,
        required=False)

    class Meta:
        model = Client
        fields = '__all__'
        read_only = ('created_by',)

# endregion
