from django.db.models import IntegerChoices


class UserRole(IntegerChoices):
    ALL = 1
    MANAGER = 2
    REALTOR = 3


class RealtyType(IntegerChoices):
    SALE = 1
    RENT = 2
