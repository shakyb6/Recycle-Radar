# Generated by Django 4.2.11 on 2024-03-30 12:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0036_reg_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reg',
            name='user',
        ),
        migrations.AlterField(
            model_name='reg',
            name='username',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL),
        ),
    ]
