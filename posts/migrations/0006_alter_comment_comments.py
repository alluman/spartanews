# Generated by Django 4.2 on 2024-05-07 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_rename_conments_comment_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comments',
            field=models.CharField(max_length=255),
        ),
    ]
