# Generated by Django 3.0.6 on 2020-06-18 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='extras',
            field=models.IntegerField(null=True),
        ),
    ]
