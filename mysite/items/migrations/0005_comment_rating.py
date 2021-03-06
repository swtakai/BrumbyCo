# Generated by Django 3.1.7 on 2021-04-09 03:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0004_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='rating',
            field=models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(5, 'Rating must be between one and 5 stars'), django.core.validators.MinValueValidator(1, 'Rating must be between one and 5 stars')]),
        ),
    ]
