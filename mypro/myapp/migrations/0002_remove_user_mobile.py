# Generated by Django 4.2.2 on 2023-07-03 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='mobile',
        ),
    ]
