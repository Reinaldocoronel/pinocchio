# Generated by Django 3.0.6 on 2020-06-23 18:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_auto_20200623_1345'),
    ]

    operations = [
        migrations.RenameField(
            model_name='toppings',
            old_name='include_in',
            new_name='items',
        ),
    ]
