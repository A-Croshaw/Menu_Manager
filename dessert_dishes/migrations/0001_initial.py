# Generated by Django 3.2.20 on 2024-01-02 21:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('desserts', '0004_alter_dessert_dessert_type'),
        ('dessert_sauces', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DessertDish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dessert_dish_name', models.CharField(max_length=300)),
                ('dessert_dish_description', models.CharField(max_length=500)),
                ('dessert_dish_type', models.CharField(choices=[('Cold Dessert', 'Cold Dessert'), ('Hot Dessert', 'Hot Dessert')], default='Cold Dessert', max_length=50)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dessert_dish_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['dessert_dish_name'],
            },
        ),
        migrations.CreateModel(
            name='DessertDishSauce',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dessert_dish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dessert_dishes.dessertdish')),
                ('dessert_dish_sauce', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dessertsauce', to='dessert_sauces.dessertsauce')),
            ],
        ),
        migrations.CreateModel(
            name='DessertDishElement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dessert_dish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dessert_dishes.dessertdish')),
                ('dessert_dish_element', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dessertelement', to='desserts.dessert')),
            ],
        ),
    ]
