# Generated by Django 3.0.1 on 2019-12-31 10:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pollution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime(2019, 12, 31, 16, 1, 24, 649552))),
            ],
        ),
    ]
