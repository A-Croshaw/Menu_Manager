# Generated by Django 3.2.20 on 2024-01-12 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dessert_sauces', '0007_auto_20240112_1200'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dessertsauceingredients',
            old_name='dessert_sauce_key',
            new_name='dessertsauce',
        ),
        migrations.RenameField(
            model_name='dessertsaucemethod',
            old_name='dessert_sauce_key',
            new_name='dessertsauce',
        ),
    ]