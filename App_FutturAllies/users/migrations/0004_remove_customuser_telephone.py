# Generated by Django 4.2.15 on 2024-08-26 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_rename_tel_customuser_telephone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='telephone',
        ),
    ]