# Generated by Django 2.1.2 on 2018-11-02 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Criminal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, upload_to='images/')),
                ('first_name', models.CharField(max_length=250)),
                ('last_name', models.CharField(blank=True, max_length=250)),
                ('wanted_level', models.TextField(blank=True)),
                ('nick_name', models.CharField(blank=True, max_length=250)),
                ('obligations', models.TextField(blank=True)),
                ('crime_areas', models.TextField(blank=True)),
                ('prize_money', models.TextField(default='0', null=True)),
                ('number_of_times_tapped', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
