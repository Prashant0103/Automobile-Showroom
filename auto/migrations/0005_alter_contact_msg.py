# Generated by Django 3.2.8 on 2022-03-12 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auto', '0004_auto_20220304_2235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='msg',
            field=models.TextField(max_length=200),
        ),
    ]
