# Generated by Django 2.2.7 on 2020-03-16 19:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_auto_20200317_0100'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
