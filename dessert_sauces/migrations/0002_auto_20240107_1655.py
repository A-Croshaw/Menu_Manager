# Generated by Django 3.2.20 on 2024-01-07 16:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
        ('dessert_sauces', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dessertsauce',
            name='dessert_sauce_type',
            field=models.CharField(choices=[('Cold Sauce', 'Cold Sauce'), ('Hot Sauce', 'Hot Sauce')], default='Cold Dessert Sauce', max_length=50),
        ),
        migrations.AlterField(
            model_name='dessertsauceingredients',
            name='dessert_sauce_ingredient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dessert_sauce_ing', to='products.product'),
        ),
        migrations.AlterField(
            model_name='dessertsauceingredients',
            name='dessert_sauce_unit_type',
            field=models.CharField(choices=[('gr', 'gr'), ('Kg', 'Kg'), ('ml', 'ml'), ('lt', 'lt')], default='gr', max_length=50),
        ),
    ]
