# Generated by Django 4.0.1 on 2023-12-16 09:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reg',
            old_name='PhoneCode',
            new_name='phone',
        ),
    ]
