# Generated by Django 4.1.2 on 2022-10-31 11:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rentalCarSystem', '0012_client_address'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='address',
            new_name='address1',
        ),
    ]