# Generated by Django 3.2.20 on 2024-01-12 09:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('starter_dishes', '0002_alter_starterdish_starter_dish_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='starterdish',
            name='user',
        ),
    ]
