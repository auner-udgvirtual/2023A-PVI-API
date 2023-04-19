# Generated by Django 4.1.8 on 2023-04-17 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='comments',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='eta',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='received_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='ticket',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
