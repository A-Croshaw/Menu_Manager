# Generated by Django 3.2.20 on 2023-10-11 11:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Dessert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dessert_name', models.CharField(max_length=300)),
                ('dessert_description', models.CharField(max_length=500)),
                ('dessert_type', models.CharField(choices=[('Soup', 'Soup'), ('Cold_Dessert', 'Cold_Dessert'), ('Hot Dessert', 'Hot Dessert'), ('Hot Sauce', 'Hot Sauce'), ('Cold Sauce', 'Cold Sauce')], default='soup', max_length=50)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dessert_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['dessert_name'],
            },
        ),
        migrations.CreateModel(
            name='DessertMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dessert_Steps', models.CharField(max_length=500)),
                ('dessert', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='desserts.dessert')),
            ],
        ),
        migrations.CreateModel(
            name='DessertIngredients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dessert_quantity', models.DecimalField(decimal_places=2, max_digits=10)),
                ('dessert_unit_type', models.CharField(choices=[('gr', 'gr'), ('Kg', 'Kg'), ('Oz', 'Oz'), ('lb', 'lSb'), ('tsp', 'tsp'), ('Tbsp', 'Tbsp'), ('floz', 'floz'), ('Pint', 'Pint'), ('ml', 'ml'), ('lt', 'lt')], default='gr', max_length=50)),
                ('dessert', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='desserts.dessert')),
                ('dessert_ingredient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='desserting', to='products.product')),
            ],
        ),
    ]
