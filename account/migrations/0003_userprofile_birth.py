# Generated by Django 2.0 on 2018-01-30 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_remove_userprofile_birth'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='birth',
            field=models.DateField(blank=True, null=True),
        ),
    ]