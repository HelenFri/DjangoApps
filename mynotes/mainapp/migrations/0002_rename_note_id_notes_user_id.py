# Generated by Django 4.2.5 on 2023-10-05 05:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notes',
            old_name='Note_id',
            new_name='User_id',
        ),
    ]
