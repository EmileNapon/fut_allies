# Generated by Django 4.2 on 2024-11-26 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Formation', '0015_alter_webinar_startdatetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webinar',
            name='registrationDeadline',
            field=models.CharField(default='10 Octobre 2024', max_length=200),
        ),
    ]