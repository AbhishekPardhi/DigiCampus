# Generated by Django 4.0.3 on 2022-03-28 06:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0004_profile_order_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='is_prof',
            new_name='is_security',
        ),
    ]
