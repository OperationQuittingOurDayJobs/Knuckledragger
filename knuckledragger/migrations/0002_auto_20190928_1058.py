# Generated by Django 2.2.3 on 2019-09-28 15:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('knuckledragger', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rarity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quality', models.CharField(default='mundane', max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(default='normal', max_length=16)),
            ],
        ),
        migrations.AlterField(
            model_name='greeting',
            name='when',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date created'),
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.FloatField(default=0)),
                ('max_durability', models.FloatField(default=0)),
                ('current_durability', models.FloatField(default=0)),
                ('name', models.CharField(max_length=50)),
                ('price', models.FloatField(default=0)),
                ('description', models.TextField(max_length=300)),
                ('material', models.CharField(max_length=20)),
                ('x_dimension', models.IntegerField(default=0)),
                ('y_dimension', models.IntegerField(default=0)),
                ('rarity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='knuckledragger.Rarity')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='knuckledragger.Status')),
            ],
        ),
    ]