# Generated by Django 3.0.2 on 2020-01-31 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('breweries', '0025_remove_food_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='image',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
