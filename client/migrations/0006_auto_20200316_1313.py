# Generated by Django 2.2.7 on 2020-03-16 07:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0005_auto_20200316_1309'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='Gst',
        ),
        migrations.RemoveField(
            model_name='client',
            name='Tel',
        ),
    ]
