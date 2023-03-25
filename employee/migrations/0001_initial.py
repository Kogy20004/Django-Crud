# Generated by Django 4.1.7 on 2023-03-24 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eid', models.CharField(max_length=20)),
                ('etype', models.CharField(max_length=25)),
                ('eprice', models.CharField(max_length=100)),
                ('ecsell', models.CharField(max_length=50)),
                ('etypeiden', models.CharField(max_length=10)),
                ('eperson', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'employee',
            },
        ),
    ]
