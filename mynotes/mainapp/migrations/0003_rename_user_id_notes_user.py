# Generated by Django 4.2.5 on 2023-10-05 05:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_rename_note_id_notes_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notes',
            old_name='User_id',
            new_name='User',
        ),
    ]
