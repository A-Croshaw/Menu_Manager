# Generated by Django 3.2.20 on 2024-01-12 09:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('desserts', '0005_auto_20240107_1655'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dessert',
            name='user',
        ),
    ]
