# Generated by Django 3.2.20 on 2024-01-12 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dessert_sauces', '0006_auto_20240112_1148'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dessertsauceingredients',
            old_name='dessert_sauce',
            new_name='dessert_sauce_key',
        ),
        migrations.RenameField(
            model_name='dessertsaucemethod',
            old_name='dessert_sauce',
            new_name='dessert_sauce_key',
        ),
    ]