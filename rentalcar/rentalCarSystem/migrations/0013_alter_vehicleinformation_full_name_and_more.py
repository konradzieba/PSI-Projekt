# Generated by Django 4.1.3 on 2022-11-14 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentalCarSystem', '0012_client_full_name_payment_full_name_vehicle_full_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicleinformation',
            name='full_name',
            field=models.CharField(blank=True, editable=False, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='vehiclespecification',
            name='full_name',
            field=models.CharField(blank=True, editable=False, max_length=500, null=True),
        ),
    ]
