# Generated by Django 3.0.2 on 2020-01-27 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('breweries', '0003_auto_20200127_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beer',
            name='abv',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='beer',
            name='description',
            field=models.TextField(max_length=255),
        ),
    ]
