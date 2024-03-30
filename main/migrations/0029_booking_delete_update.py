# Generated by Django 4.2.11 on 2024-03-30 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0028_delete_member_remove_assign_ward_remove_reg_ward_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scrap_name', models.CharField(max_length=30)),
                ('scrap_quantity', models.IntegerField()),
                ('date', models.DateField()),
                ('location', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='update',
        ),
    ]
