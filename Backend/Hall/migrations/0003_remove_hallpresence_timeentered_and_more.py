# Generated by Django 4.0.3 on 2022-03-18 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Hall', '0002_alter_hallpresence_user_visiting'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hallpresence',
            name='timeEntered',
        ),
        migrations.RemoveField(
            model_name='hallpresence',
            name='timeExit',
        ),
    ]
