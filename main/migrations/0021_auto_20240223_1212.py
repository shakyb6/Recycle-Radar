# Generated by Django 3.0.5 on 2024-02-23 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_remove_update_fname'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='ward',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reg',
            name='ward',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
