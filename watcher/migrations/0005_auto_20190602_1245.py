# Generated by Django 2.1.7 on 2019-06-02 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watcher', '0004_equity_per_change'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equity',
            name='symbol',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
