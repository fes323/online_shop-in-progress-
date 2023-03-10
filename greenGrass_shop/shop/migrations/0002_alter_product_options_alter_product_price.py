# Generated by Django 4.1.4 on 2022-12-24 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('name',), 'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, max_length=0),
        ),
    ]
