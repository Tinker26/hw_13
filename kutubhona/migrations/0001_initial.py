# Generated by Django 3.2.9 on 2021-11-19 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Muallif',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=200)),
                ('reyting', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Kitob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=100)),
                ('betlar_soni', models.IntegerField()),
                ('muallif', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='kitoblar', to='kutubhona.muallif')),
            ],
        ),
    ]
