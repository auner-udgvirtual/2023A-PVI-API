# Generated by Django 4.1.8 on 2023-04-17 22:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilefeeditem',
            name='available_at',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='profilefeeditem',
            name='then_will_working_on',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='profilefeeditem',
            name='working_on',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
    ]
