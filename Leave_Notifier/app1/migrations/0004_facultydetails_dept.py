# Generated by Django 3.0.5 on 2020-10-31 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_auto_20201031_0057'),
    ]

    operations = [
        migrations.AddField(
            model_name='facultydetails',
            name='dept',
            field=models.CharField(default='CSE', max_length=40),
        ),
    ]
