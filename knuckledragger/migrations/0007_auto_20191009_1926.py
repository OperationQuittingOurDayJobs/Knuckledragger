# Generated by Django 2.2.3 on 2019-10-10 00:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('knuckledragger', '0006_auto_20191009_1712'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='character',
            name='attributes',
        ),
        migrations.RemoveField(
            model_name='character',
            name='equipment_slots',
        ),
        migrations.RemoveField(
            model_name='character',
            name='race',
        ),
    ]
