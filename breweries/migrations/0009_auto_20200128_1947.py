# Generated by Django 3.0.2 on 2020-01-28 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('breweries', '0008_food_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='brewery',
            name='city',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='brewery',
            name='zipcode',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
