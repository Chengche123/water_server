# Generated by Django 4.0.2 on 2022-04-30 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('water', '0005_userextend_is_access'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alarmthreshold',
            name='method',
            field=models.SmallIntegerField(default=0),
        ),
    ]