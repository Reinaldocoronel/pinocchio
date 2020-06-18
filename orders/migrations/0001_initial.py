# Generated by Django 3.0.6 on 2020-06-18 17:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, unique=True)),
                ('tipe', models.CharField(max_length=10)),
                ('extras', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Topings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Prices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('tipe', models.CharField(max_length=4)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Items')),
            ],
        ),
    ]
