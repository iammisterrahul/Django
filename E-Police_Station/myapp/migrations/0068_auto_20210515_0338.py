# Generated by Django 3.2 on 2021-05-14 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0067_auto_20210515_0338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='constable',
            name='first_name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='constable',
            name='last_name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='constable',
            name='username',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]