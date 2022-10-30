# Generated by Django 4.1.2 on 2022-10-25 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentalCarSystem', '0005_alter_payment_card_number_alter_payment_cash_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='VehicleInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year_of_production', models.IntegerField(choices=[(2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022)], default=2022)),
                ('license_plate_number', models.CharField(max_length=9)),
                ('vin_number', models.CharField(max_length=17)),
                ('date_of_the_review', models.DateField()),
                ('condition_comment', models.CharField(max_length=250, null=True)),
                ('mileage', models.IntegerField()),
                ('last_service', models.IntegerField(null=True)),
            ],
        ),
    ]
