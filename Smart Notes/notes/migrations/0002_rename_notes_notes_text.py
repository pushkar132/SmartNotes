# Generated by Django 4.2.1 on 2023-05-31 11:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notes',
            old_name='notes',
            new_name='text',
        ),
    ]
