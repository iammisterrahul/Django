# Generated by Django 3.2 on 2021-05-06 19:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0047_inspector_login_service_officers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inspector',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.inspector_login'),
        ),
    ]