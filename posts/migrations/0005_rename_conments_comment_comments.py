# Generated by Django 4.2 on 2024-05-07 05:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_rename_conment_comment_conments'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='conments',
            new_name='comments',
        ),
    ]