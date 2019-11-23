# Generated by Django 2.2.7 on 2019-11-10 01:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FloorManager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('floornum', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roomnum', models.IntegerField()),
                ('floornum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='roll_call.FloorManager')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ssn', models.CharField(default='교환학생', max_length=7)),
                ('name', models.CharField(default='unknown', max_length=30)),
                ('phone', models.CharField(default='unknown', max_length=30)),
                ('mother_phone', models.CharField(default='unknown', max_length=30)),
                ('status', models.CharField(default='무단외박', max_length=10)),
                ('room_num', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='roll_call.Room')),
            ],
        ),
    ]