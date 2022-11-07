# Generated by Django 4.1.2 on 2022-10-31 11:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentalCarSystem', '0018_alter_rent_discount_in_perc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rent',
            name='deposit',
            field=models.IntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(500), django.core.validators.MaxValueValidator(100000)]),
        ),
        migrations.AlterField(
            model_name='rent',
            name='km_limit',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(999)]),
        ),
    ]