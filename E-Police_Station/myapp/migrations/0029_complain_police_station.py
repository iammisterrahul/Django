# Generated by Django 3.2 on 2021-04-27 10:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0028_fir_police_station'),
    ]

    operations = [
        migrations.AddField(
            model_name='complain',
            name='police_station',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.police_station'),
        ),
    ]
