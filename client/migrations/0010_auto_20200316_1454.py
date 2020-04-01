# Generated by Django 2.2.7 on 2020-03-16 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0009_clientbalance'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientbalance',
            name='Total_payment',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=999999, null=True),
        ),
        migrations.AddField(
            model_name='clientbalance',
            name='Total_sales',
            field=models.DecimalField(decimal_places=2, default=2, max_digits=999999),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='clientbalance',
            name='balance_payment',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=999999, null=True),
        ),
    ]
