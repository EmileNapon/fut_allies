# Generated by Django 4.2 on 2024-11-22 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_customuser_profile_pic_alter_customuser_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('apprenant', 'Apprenant'), ('employeur', 'Employeur')], default='Apprenant', max_length=10),
        ),
    ]