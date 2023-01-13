# Generated by Django 4.1.5 on 2023-01-13 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autographs', '0004_alter_address_additional_info_alter_address_city_and_more'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='person',
            constraint=models.UniqueConstraint(fields=('first_name', 'last_name'), name='unique name'),
        ),
    ]
