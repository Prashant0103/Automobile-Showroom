# Generated by Django 3.2.8 on 2022-02-24 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auto', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='type',
            field=models.CharField(choices=[('coupe', 'Coupe'), ('hatchback', 'Hatchback'), ('sedan', 'Sedan'), ('suv', 'SUV'), ('sports', 'Sports'), ('supercar', 'Supercar'), ('van', 'VAN')], default='coupe', max_length=20),
        ),
        migrations.AlterField(
            model_name='car',
            name='company',
            field=models.CharField(choices=[('bmw', 'BMW'), ('mercedes', 'Mercedes'), ('maruti', 'Maruti'), ('lamborghini', 'Lamborghini'), ('honda', 'Honda'), ('toyota', 'Toyota'), ('mahindra', 'Mahindra'), ('tata', 'Tata'), ('skoda', 'Skoda')], default='bmw', max_length=20),
        ),
    ]