from django.db import models
from django.core.exceptions import ValidationError

from utils.enums import RealtyType

_3MB = 3145728


def validate_image(value):
    file_size = value.size
    if file_size > _3MB:
        raise ValidationError(
            'The maximum file size that can be uploaded is 3MB')


class Client(models.Model):
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    additional_info = models.TextField()
    created_by = models.ForeignKey(
        'users.User', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'

    def __str__(self):
        return self.full_name


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class RealtyImage(models.Model):
    image = models.ImageField(
        upload_to='realty_image',
        height_field=None,
        width_field=None,
        max_length=None,
        null=True,
        blank=True,
        validators=[validate_image],
    )
    realty = models.ForeignKey('Realty', on_delete=models.CASCADE,
                               null=True, blank=True, related_name='realty_images')

    class Meta:
        verbose_name = 'Realty image'
        verbose_name_plural = 'Realty images'


class Realty(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    minimum_price = models.DecimalField(
        max_digits=15, decimal_places=2, default=0)
    desired_price = models.DecimalField(
        max_digits=15, decimal_places=2, default=0)
    client = models.ForeignKey(
        Client, on_delete=models.SET_NULL, related_name='realties', null=True, blank=True)
    created_by = models.ForeignKey(
        'users.User', on_delete=models.SET_NULL, null=True, blank=True)
    realty_type = models.SmallIntegerField(
        choices=RealtyType.choices, null=True, blank=True)

    class Meta:
        verbose_name = 'Realty'
        verbose_name_plural = 'Realties'
