# Generated by Django 2.2.7 on 2020-03-16 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0013_client_gst_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='Tel',
            field=models.IntegerField(blank=True, max_length=10, null=True),
        ),
    ]
