# Generated by Django 3.0.2 on 2020-01-28 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('breweries', '0009_auto_20200128_1947'),
    ]

    operations = [
        migrations.AddField(
            model_name='beer',
            name='image',
            field=models.TextField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]