# Generated by Django 3.2 on 2021-08-26 10:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_profile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
