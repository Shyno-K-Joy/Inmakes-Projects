# Generated by Django 4.2.7 on 2023-12-04 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1996-04-24'),
            preserve_default=False,
        ),
    ]
