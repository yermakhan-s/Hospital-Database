# Generated by Django 4.1.2 on 2022-11-18 15:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sqlapp', '0014_alter_discover_first_enc_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discover',
            name='first_enc_date',
            field=models.DateField(default=datetime.date(2022, 11, 18)),
        ),
    ]
