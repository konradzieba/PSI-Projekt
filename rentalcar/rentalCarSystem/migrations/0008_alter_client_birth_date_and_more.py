# Generated by Django 4.1.2 on 2022-10-26 09:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentalCarSystem', '0007_alter_client_birth_date_alter_client_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='birth_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='client',
            name='driver_licence_number',
            field=models.CharField(max_length=13, unique=True, validators=[django.core.validators.MinLengthValidator(11), django.core.validators.MinLengthValidator(11)]),
        ),
        migrations.AlterField(
            model_name='client',
            name='email',
            field=models.EmailField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='pesel',
            field=models.CharField(max_length=11, unique=True, validators=[django.core.validators.MinLengthValidator(11), django.core.validators.MinLengthValidator(11)]),
        ),
        migrations.AlterField(
            model_name='client',
            name='phone_numer',
            field=models.CharField(max_length=15, unique=True, validators=[django.core.validators.MinLengthValidator(9), django.core.validators.MinLengthValidator(11)]),
        ),
    ]
