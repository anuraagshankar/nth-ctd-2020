# Generated by Django 3.0.2 on 2020-02-03 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nth', '0003_player_last_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='last_time',
            field=models.DateField(auto_now=True),
        ),
    ]
