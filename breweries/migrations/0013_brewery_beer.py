# Generated by Django 3.0.2 on 2020-01-28 21:24

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('breweries', '0012_remove_brewery_beer'),
    ]

    operations = [
        migrations.AddField(
            model_name='brewery',
            name='beer',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), blank=True, default=[1, 2, 3, 4, 5, 6], size=None),
            preserve_default=False,
        ),
    ]
