# Generated by Django 4.0.2 on 2022-04-10 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('water', '0002_hx2022_alter_hx2021_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hx2022',
            name='udatetime',
            field=models.DateTimeField(auto_now_add=True, db_column='uDateTime', null=True),
        ),
    ]