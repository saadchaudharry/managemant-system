# Generated by Django 2.2.7 on 2020-03-16 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0006_auto_20200316_1313'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='Initial_Balance',
            field=models.IntegerField(default=423, max_length=99999),
            preserve_default=False,
        ),
    ]
