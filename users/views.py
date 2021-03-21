from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.decorators import action
from utils.base_viewset import BaseModelViewSet

from .serializers import UserSerializer, UserListSerializer, ChangePasswordSerializer
from .models import User


class UserViewSet(BaseModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = User.objects.all()
    default_serializer_class = UserSerializer
    serializer_classes = {
        'list': UserListSerializer
    }

    @action(methods=['get'], detail=False, url_path='me', permission_classes=[IsAuthenticated])
    def current_user(self, request, *args, **kwargs):
        return Response({'user': UserSerializer(request.user).data}, status.HTTP_200_OK)

    @action(methods=['get'], detail=False, url_path='change-password', permission_classes=[IsAuthenticated])
    def change_password(self, request, *args, **kwargs):
        serializer = ChangePasswordSerializer(
            data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'message': 'Password has been updated'}, status.HTTP_200_OK)
