from rest_framework import status, parsers
from rest_framework.response import Response
from rest_framework.decorators import action
from utils.base_viewset import BaseModelViewSet

from .serializers import RealtyListSerializer, RealtySerializer, ClientListSerializer, ClientSerializer
from .models import Category, Realty, RealtyImage, Client
from utils.permissions import RealtyPermission, IsOwnerOrReadOnly


class RealtyViewSet(BaseModelViewSet):
    permission_classes = [RealtyPermission, IsOwnerOrReadOnly]
    parser_classes = (parsers.MultiPartParser, parsers.FormParser,)
    queryset = Realty.objects.all()

    default_serializer_class = RealtySerializer
    serializer_classes = {
        'list': RealtyListSerializer
    }

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    @action(detail=True, methods=['post'], url_path='upload-images')
    def upload_images(self, request, pk, *args, **kwargs):
        for image in request.FILES.getlist('image'):
            RealtyImage.objects.create(realty_id=pk, image=image)

        return Response(status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['delete'], url_path=r'delete-image/(?P<image_pk>\w+)')
    def delete_image(self, request, pk, image_pk, *args, **kwargs):
        RealtyImage.objects.filter(id=image_pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ClientViewSet(BaseModelViewSet):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Client.objects.all()

    default_serializer_class = ClientSerializer
    serializer_classes = {
        'list': ClientListSerializer
    }

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
