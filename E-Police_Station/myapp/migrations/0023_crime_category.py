# Generated by Django 3.2 on 2021-04-26 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0022_inspector'),
    ]

    operations = [
        migrations.CreateModel(
            name='Crime_Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crime_category', models.CharField(max_length=256)),
            ],
        ),
    ]
