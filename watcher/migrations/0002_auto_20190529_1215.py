# Generated by Django 2.1.7 on 2019-05-29 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watcher', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='derivative',
            name='pinned',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='equity',
            name='pinned',
            field=models.BooleanField(default=False),
        ),
    ]