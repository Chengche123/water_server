# Generated by Django 4.0.2 on 2022-05-12 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('water', '0009_rename_threshold_value_alarmthreshold_threshold_value_max_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='alarmthreshold',
            name='last_alert_datetime',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
