# Generated by Django 3.2.20 on 2024-01-12 09:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_dishes', '0003_maindishside'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='maindish',
            name='user',
        ),
    ]
