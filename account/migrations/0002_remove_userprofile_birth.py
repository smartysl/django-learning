# Generated by Django 2.0 on 2018-01-30 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='birth',
        ),
    ]
