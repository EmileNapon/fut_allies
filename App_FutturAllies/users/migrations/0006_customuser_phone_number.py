# Generated by Django 4.2.15 on 2024-08-28 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_remove_customuser_user_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, null=True, unique=True),
        ),
    ]