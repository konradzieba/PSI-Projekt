# Generated by Django 4.1.3 on 2022-11-13 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentalCarSystem', '0008_alter_rent_deposit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rent',
            name='final_price',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='(updated on save)', max_digits=8, null=True),
        ),
    ]
