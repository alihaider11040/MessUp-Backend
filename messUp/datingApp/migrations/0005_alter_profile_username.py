# Generated by Django 4.0.5 on 2022-08-11 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datingApp', '0004_alter_zodiac_zodiac'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='username',
            field=models.CharField(blank=True, max_length=200, null=True, unique=True),
        ),
    ]