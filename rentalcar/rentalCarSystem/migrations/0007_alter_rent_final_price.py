# Generated by Django 4.1.3 on 2022-11-13 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentalCarSystem', '0006_alter_rent_final_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rent',
            name='final_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True),
        ),
    ]
