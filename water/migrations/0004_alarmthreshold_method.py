# Generated by Django 4.0.2 on 2022-04-27 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('water', '0003_alter_alarmthreshold_threshold_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='alarmthreshold',
            name='method',
            field=models.SmallIntegerField(default=2),
        ),
    ]
