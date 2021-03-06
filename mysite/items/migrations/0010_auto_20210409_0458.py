# Generated by Django 3.1.7 on 2021-04-09 04:58

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0009_auto_20210409_0449'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='rating',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='review',
        ),
        migrations.AddField(
            model_name='comment',
            name='text',
            field=models.TextField(default=django.utils.timezone.now, validators=[django.core.validators.MinLengthValidator(3, 'Comment must be greater than 3 characters')]),
            preserve_default=False,
        ),
    ]
