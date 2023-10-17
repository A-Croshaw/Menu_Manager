# Generated by Django 3.2.20 on 2023-10-17 13:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sauce',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sauce_name', models.CharField(max_length=300)),
                ('sauce_description', models.CharField(max_length=500)),
                ('sauce_type', models.CharField(choices=[('Cold Sauce', 'Cold Sauce'), ('Hot Sauce', 'Hot Sauce')], default='soup', max_length=50)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sauce_recipe_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SauceMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sauce_Steps', models.CharField(max_length=500)),
                ('sauce', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sauces.sauce')),
            ],
        ),
        migrations.CreateModel(
            name='SauceIngredients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sauce_quantity', models.DecimalField(decimal_places=2, max_digits=10)),
                ('sauce_unit_type', models.CharField(choices=[('gr', 'gr'), ('kg', 'Kg'), ('oz', 'Oz'), ('lb', 'Lb'), ('tsp', 'tsp'), ('Tbsp', 'Tbsp'), ('floz', 'floz'), ('pint', 'Pint'), ('ml', 'ml'), ('lt', 'lt')], default='gr', max_length=50)),
                ('sauce', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sauces.sauce')),
                ('sauce_ingredient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sauceing', to='products.product')),
            ],
        ),
    ]
