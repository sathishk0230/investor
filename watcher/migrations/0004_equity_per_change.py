# Generated by Django 2.1.7 on 2019-05-31 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watcher', '0003_auto_20190531_1300'),
    ]

    operations = [
        migrations.AddField(
            model_name='equity',
            name='per_change',
            field=models.FloatField(default=0.0),
        ),
    ]
