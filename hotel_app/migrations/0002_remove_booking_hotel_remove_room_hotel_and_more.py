# Generated by Django 4.1.2 on 2022-10-06 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='hotel',
        ),
        migrations.RemoveField(
            model_name='room',
            name='hotel',
        ),
        migrations.AddField(
            model_name='room',
            name='room_size',
            field=models.FloatField(default=1),
        ),
        migrations.DeleteModel(
            name='Hotel',
        ),
    ]