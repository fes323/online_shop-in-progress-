# Generated by Django 4.1.5 on 2023-01-08 22:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_order_phone_number_alter_order_address_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='postal_code',
        ),
    ]