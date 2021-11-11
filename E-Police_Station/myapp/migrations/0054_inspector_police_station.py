# Generated by Django 3.2 on 2021-05-07 17:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0053_service_officers'),
    ]

    operations = [
        migrations.AddField(
            model_name='inspector',
            name='police_station',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.police_station'),
        ),
    ]
