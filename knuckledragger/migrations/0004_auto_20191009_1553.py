# Generated by Django 2.2.3 on 2019-10-09 20:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('knuckledragger', '0003_attributes_brawny_character_races_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brawny',
            name='type',
        ),
        migrations.RemoveField(
            model_name='character',
            name='attributes',
        ),
        migrations.RemoveField(
            model_name='character',
            name='race',
        ),
        migrations.DeleteModel(
            name='Greeting',
        ),
        migrations.RemoveField(
            model_name='item',
            name='rarity',
        ),
        migrations.RemoveField(
            model_name='item',
            name='status',
        ),
        migrations.RemoveField(
            model_name='room',
            name='user',
        ),
        migrations.DeleteModel(
            name='Attributes',
        ),
        migrations.DeleteModel(
            name='Brawny',
        ),
        migrations.DeleteModel(
            name='Character',
        ),
        migrations.DeleteModel(
            name='Item',
        ),
        migrations.DeleteModel(
            name='Races',
        ),
        migrations.DeleteModel(
            name='Rarity',
        ),
        migrations.DeleteModel(
            name='Room',
        ),
        migrations.DeleteModel(
            name='Status',
        ),
        migrations.DeleteModel(
            name='Type',
        ),
    ]
