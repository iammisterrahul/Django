# Generated by Django 3.1.8 on 2021-04-15 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_auto_20210415_1305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complain',
            name='complain_Date_and_Time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]