# Generated by Django 4.2.11 on 2024-03-30 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0034_alter_reg_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reg',
            name='username',
            field=models.CharField(max_length=30),
        ),
    ]
