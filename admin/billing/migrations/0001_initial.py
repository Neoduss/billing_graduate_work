# Generated by Django 3.2 on 2022-07-29 15:30

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.RunSQL(
            sql='CREATE SCHEMA IF NOT EXISTS admin;',
            reverse_sql='DROP SCHEMA IF EXISTS admin CASCADE;',
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('value', models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='product price')),
                ('currency', models.CharField(max_length=5, verbose_name='price currency')),
                ('description', models.TextField(verbose_name='description of price')),
                ('is_active', models.BooleanField(default=False, verbose_name='is price active')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
            ],
            options={
                'verbose_name': 'price',
                'verbose_name_plural': 'prices',
                'db_table': 'admin"."price',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(db_index=True, max_length=200, verbose_name='name of product')),
                ('description', models.TextField(verbose_name='description of product')),
                ('type', models.CharField(max_length=20, verbose_name='type of product')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'products',
                'db_table': 'admin"."product',
            },
        ),
        migrations.CreateModel(
            name='ProductWithPrice',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('price', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='carts', to='billing.price', verbose_name='price')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='carts', to='billing.product', verbose_name='product')),
            ],
            options={
                'verbose_name': 'cart',
                'verbose_name_plural': 'cart',
                'db_table': 'admin"."cart',
            },
        ),
        migrations.AddField(
            model_name='price',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='prices', to='billing.product', verbose_name='product'),
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('user_id', models.UUIDField(db_index=True, verbose_name='user_id')),
                ('payment_system', models.CharField(db_index=True, max_length=20, verbose_name='payment system')),
                ('payment_status', models.CharField(max_length=50, verbose_name='payment status')),
                ('paid', models.BooleanField(verbose_name='paid')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='created at')),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='updated at')),
                ('cart', models.ManyToManyField(related_name='payments', to='billing.ProductWithPrice', verbose_name='cart')),
            ],
            options={
                'verbose_name': 'payment',
                'verbose_name_plural': 'payments',
                'db_table': 'admin"."payment',
            },
        ),
    ]
