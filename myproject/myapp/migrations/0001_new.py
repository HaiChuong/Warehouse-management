# Generated by Django 3.2.25 on 2024-12-13 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Export',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_code', models.CharField(max_length=50, unique=True)),
                ('export_date', models.DateField()),
                ('number', models.IntegerField(default=0)),
                ('customer_name', models.CharField(max_length=200)),
                ('sale_price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Import',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_code', models.CharField(max_length=50, unique=True)),
                ('import_date', models.DateField()),
                ('number', models.IntegerField(default=0)),
                ('supplier', models.CharField(max_length=200)),
                ('purchase_price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_code', models.CharField(max_length=50, unique=True)),
                ('quantity', models.IntegerField(default=0)),
                ('new', models.IntegerField(default=0)),
                ('old', models.IntegerField(default=0)),
                ('unit', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_code', models.CharField(max_length=50, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('purchase_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('sale_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.IntegerField(default=0)),
            ],
        ),
    ]
