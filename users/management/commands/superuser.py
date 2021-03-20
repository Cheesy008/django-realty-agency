import logging

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError

User = get_user_model()


class Command(BaseCommand):
    help = 'Creating superuser'

    def handle(self, *args, **kwargs):
        if kwargs.get('email') is None or kwargs.get('password') is None:
            raise CommandError('Not all required parameters passed')

        if User.objects.filter(is_superuser=True).count() == 0:
            User.objects.create_superuser(kwargs.get('email'),
                                          kwargs.get('password'))

    def add_arguments(self, parser):
        parser.add_argument('email', type=str, help='User email')
        parser.add_argument('password', type=str, help='User password')
