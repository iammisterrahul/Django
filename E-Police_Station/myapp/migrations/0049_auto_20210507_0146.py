# Generated by Django 3.2 on 2021-05-06 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0048_alter_inspector_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='constable',
            name='username',
            field=models.CharField(max_length=256, unique=True),
        ),
        migrations.AlterField(
            model_name='inspector_login',
            name='username',
            field=models.CharField(max_length=256, unique=True),
        ),
        migrations.AlterField(
            model_name='sub_inspector',
            name='username',
            field=models.CharField(max_length=256, unique=True),
        ),
    ]