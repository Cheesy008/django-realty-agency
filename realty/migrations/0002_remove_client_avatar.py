# Generated by Django 3.1.7 on 2021-03-20 18:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('realty', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='avatar',
        ),
    ]