# Generated by Django 3.1.7 on 2021-04-05 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_auto_20210405_0336'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='content_type',
            field=models.CharField(blank=True, help_text='The MIMEType of the file', max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='picture',
            field=models.BinaryField(blank=True, editable=True, null=True),
        ),
    ]
