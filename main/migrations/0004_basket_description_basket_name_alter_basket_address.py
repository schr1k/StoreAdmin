# Generated by Django 5.0 on 2023-12-09 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_basket_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='basket',
            name='description',
            field=models.CharField(default='Не указано', max_length=100),
        ),
        migrations.AddField(
            model_name='basket',
            name='name',
            field=models.CharField(default='Не указано', max_length=50),
        ),
        migrations.AlterField(
            model_name='basket',
            name='address',
            field=models.CharField(default='Не указан', max_length=100),
        ),
    ]
