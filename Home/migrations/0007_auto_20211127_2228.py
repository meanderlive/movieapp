# Generated by Django 3.2 on 2021-11-27 18:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0006_auto_20211126_0139'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='serial',
            name='director',
        ),
        migrations.RemoveField(
            model_name='serial',
            name='episode',
        ),
        migrations.RemoveField(
            model_name='serial',
            name='genre',
        ),
        migrations.RemoveField(
            model_name='serial',
            name='season',
        ),
        migrations.DeleteModel(
            name='Episode',
        ),
        migrations.DeleteModel(
            name='Season',
        ),
        migrations.DeleteModel(
            name='Serial',
        ),
    ]
