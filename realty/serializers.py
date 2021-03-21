from django.core.exceptions import ValidationError
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


class RealtyClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'email', 'full_name', 'phone_number')


class RealtySerializer(serializers.ModelSerializer):
    client = PresentablePrimaryKeyRelatedField(
        presentation_serializer=RealtyClientSerializer,
        queryset=Client.objects.all(),
        many=False,
        required=True
    )
    realty_images = RealtyImageSerializer(
        many=True, read_only=True)

    class Meta:
        model = Realty
        fields = '__all__'
        read_only = ('created_by',)

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

    def validate(self, attrs):
        attrs = super().validate(attrs)
        realties = attrs.get('realties')

        for realty in realties:
            if realty.client:
                raise ValidationError(
                    {'error': f'{realty} alredy linked to client'})

        return attrs

# endregion
