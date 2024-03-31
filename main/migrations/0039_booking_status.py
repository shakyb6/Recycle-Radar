# Generated by Django 4.2.11 on 2024-03-30 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0038_delete_coordinate'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Cancelled', 'Cancelled'), ('Completed', 'Completed')], default='Pending', max_length=20),
        ),
    ]
