# Generated by Django 4.0.2 on 2022-04-27 07:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('water', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlarmThreshold',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('threshold_value', models.FloatField()),
                ('sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alarm_threshold', to='water.usensor')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alarm_threshold', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'alarm_threshold',
            },
        ),
    ]
