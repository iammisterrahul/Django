# Generated by Django 3.2 on 2021-05-08 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0057_auto_20210508_2207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complain',
            name='Date_and_Time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]