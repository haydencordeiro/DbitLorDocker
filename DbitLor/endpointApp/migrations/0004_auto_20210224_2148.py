# Generated by Django 3.1.6 on 2021-02-24 21:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('endpointApp', '0003_auto_20210224_2144'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentprofile',
            name='dept',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='endpointApp.departement'),
        ),
        migrations.AddField(
            model_name='studentprofile',
            name='studentID',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='studentprofile',
            name='yearofpassout',
            field=models.CharField(max_length=4, null=True),
        ),
    ]
