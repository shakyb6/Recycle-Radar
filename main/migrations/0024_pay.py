# Generated by Django 3.0.5 on 2024-02-23 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_assign_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='pay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('phonenumber', models.CharField(max_length=30)),
                ('membername', models.CharField(max_length=30)),
                ('price', models.CharField(max_length=30)),
            ],
        ),
    ]
