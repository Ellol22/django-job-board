# Generated by Django 5.1.7 on 2025-03-19 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='job_type',
            field=models.CharField(choices=[('Full_time', 'Full_time'), ('Part_Time', 'Part_Time')], default='', max_length=15),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='job',
            name='title',
            field=models.CharField(max_length=40),
        ),
    ]
