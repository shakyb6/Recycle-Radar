# Generated by Django 3.0.5 on 2024-02-19 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_assign_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='update',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('area', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=30)),
            ],
        ),
    ]
