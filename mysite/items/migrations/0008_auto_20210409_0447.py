# Generated by Django 3.1.7 on 2021-04-09 04:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0007_auto_20210409_0443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='review',
            field=models.TextField(null=True, validators=[django.core.validators.MinLengthValidator(3, 'Comment must be greater than 3 characters')]),
        ),
    ]
