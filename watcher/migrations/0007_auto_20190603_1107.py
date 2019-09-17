# Generated by Django 2.1.7 on 2019-06-03 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watcher', '0006_auto_20190602_1250'),
    ]

    operations = [
        migrations.RenameField(
            model_name='equity',
            old_name='per_change',
            new_name='buy_per_change',
        ),
        migrations.RenameField(
            model_name='equity',
            old_name='watch_price',
            new_name='buy_watch_price',
        ),
        migrations.AddField(
            model_name='equity',
            name='sell_per_change',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='equity',
            name='sell_watch_price',
            field=models.FloatField(default=0.0),
        ),
    ]