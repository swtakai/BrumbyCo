# Generated by Django 3.1.7 on 2021-04-11 05:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0012_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='ip',
        ),
        migrations.RemoveField(
            model_name='review',
            name='status',
        ),
    ]