# Generated by Django 3.2.20 on 2024-01-11 15:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dessert_sauces', '0002_auto_20240107_1655'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dessertsauceingredients',
            old_name='dessert_sauce',
            new_name='dessert_sauce_name',
        ),
        migrations.RenameField(
            model_name='dessertsaucemethod',
            old_name='dessert_sauce',
            new_name='dessert_sauce_name',
        ),
    ]
