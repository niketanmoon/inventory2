# Generated by Django 2.0.1 on 2018-01-05 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tims', '0007_auto_20180105_0011'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='computer',
            unique_together={('ip_address', 'SerialKey', 'HostName')},
        ),
    ]
