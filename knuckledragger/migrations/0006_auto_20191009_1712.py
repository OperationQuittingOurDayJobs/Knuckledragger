# Generated by Django 2.2.3 on 2019-10-09 22:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('knuckledragger', '0005_character'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attributes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brawny', models.PositiveSmallIntegerField(default=0)),
                ('sturdy', models.PositiveSmallIntegerField(default=0)),
                ('speedy', models.PositiveSmallIntegerField(default=0)),
                ('nerdy', models.PositiveSmallIntegerField(default=0)),
                ('balky', models.PositiveSmallIntegerField(default=0)),
                ('wily', models.PositiveSmallIntegerField(default=0)),
                ('pritty', models.PositiveSmallIntegerField(default=0)),
                ('gritty', models.PositiveSmallIntegerField(default=0)),
                ('witty', models.PositiveSmallIntegerField(default=0)),
                ('beastly', models.PositiveSmallIntegerField(default=0)),
                ('techy', models.PositiveSmallIntegerField(default=0)),
                ('outdoorsy', models.PositiveSmallIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='EquipmentSlots',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head', models.BooleanField(default=False)),
                ('neck', models.BooleanField(default=False)),
                ('shoulder', models.BooleanField(default=False)),
                ('chest', models.BooleanField(default=False)),
                ('arm', models.BooleanField(default=False)),
                ('hand', models.BooleanField(default=False)),
                ('belt', models.BooleanField(default=False)),
                ('waist', models.BooleanField(default=False)),
                ('leg', models.BooleanField(default=False)),
                ('feet', models.BooleanField(default=False)),
                ('accessory', models.BooleanField(default=False)),
                ('wallet', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Race',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arrivad', models.BooleanField(default=False)),
                ('basahnin', models.BooleanField(default=False)),
                ('ferrick', models.BooleanField(default=False)),
                ('holeg', models.BooleanField(default=False)),
                ('human', models.BooleanField(default=False)),
                ('illawmi', models.BooleanField(default=False)),
                ('kassari', models.BooleanField(default=False)),
                ('khura', models.BooleanField(default=False)),
                ('mogo', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='character',
            name='age',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='character',
            name='weight',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='character',
            name='health',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='character',
            name='attributes',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='knuckledragger.Attributes'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='character',
            name='equipment_slots',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='knuckledragger.EquipmentSlots'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='character',
            name='race',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='knuckledragger.Race'),
            preserve_default=False,
        ),
    ]
