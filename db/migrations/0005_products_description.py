# Generated by Django 5.0 on 2023-12-08 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0004_rename_product_id_basket_product_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='description',
            field=models.CharField(default='Описание не указано.', max_length=100),
        ),
    ]
