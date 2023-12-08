# Generated by Django 5.0 on 2023-12-08 14:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('telegram_id', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SubCategories',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.categories')),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('subcategory_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.subcategories')),
            ],
        ),
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('address', models.CharField(max_length=100)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.products')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.users')),
            ],
        ),
    ]