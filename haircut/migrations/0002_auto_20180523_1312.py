# Generated by Django 2.0.1 on 2018-05-23 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('haircut', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='baber_name',
            new_name='barber_name',
        ),
    ]
