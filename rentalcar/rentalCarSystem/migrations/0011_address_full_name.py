# Generated by Django 4.1.3 on 2022-11-13 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentalCarSystem', '0010_alter_rent_deposit_alter_rent_final_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='full_name',
            field=models.CharField(blank=True, editable=False, max_length=100, null=True),
        ),
    ]