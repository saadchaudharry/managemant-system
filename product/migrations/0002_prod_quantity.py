# Generated by Django 2.2.7 on 2020-03-16 18:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prod_quantity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(max_length=12000)),
                ('Prod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Products')),
            ],
        ),
    ]
