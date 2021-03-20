from rest_framework import serializers, exceptions

from .models import User


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'full_name', 'role',)


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, style={'input_type': 'password'},)

    class Meta:
        model = User
        fields = ('id', 'email', 'full_name', 'role',
                  'is_staff', 'is_superuser', 'password',)

    def create(self, validated_data):
        password = validated_data.pop('password')

        instance = super().create(validated_data)
        instance.change_password(password)

        return instance

    def update(self, instance, validated_data):
        password = validated_data.pop('password')

        instance = super().update(instance, validated_data)
        instance.change_password(password)

        return instance


class ChangePasswordSerializer(serializers.Serializer):
    password = serializers.CharField(
        write_only=True, style={'input_type': 'password'})

    def save(self, **kwargs):
        password = self.validated_data['password']
        user_id = self.context['request'].user.id

        user = User.objects.get(id=user_id)
        user.change_password(password)
