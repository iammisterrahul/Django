# Generated by Django 3.2 on 2021-05-13 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0060_messing_persons'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messing_persons',
            name='height',
            field=models.CharField(max_length=10),
        ),
    ]