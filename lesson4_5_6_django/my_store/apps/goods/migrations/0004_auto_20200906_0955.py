# Generated by Django 3.1 on 2020-09-06 06:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0003_good_supplier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='good',
            name='date_receipt',
            field=models.DateField(default=datetime.datetime(2020, 9, 6, 9, 55, 24, 48990), verbose_name='дата поступления'),
        ),
    ]