# Generated by Django 2.2.7 on 2020-03-16 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_orders_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
