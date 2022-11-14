# Generated by Django 4.1.3 on 2022-11-13 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentalCarSystem', '0011_address_full_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='full_name',
            field=models.CharField(blank=True, editable=False, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='full_name',
            field=models.CharField(blank=True, editable=False, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='full_name',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='vehicleinformation',
            name='full_name',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='vehiclespecification',
            name='full_name',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='full_name',
            field=models.CharField(blank=True, editable=False, max_length=500, null=True),
        ),
    ]
