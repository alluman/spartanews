# Generated by Django 4.2 on 2024-05-07 09:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_alter_comment_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='parent_comment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='posts.comment'),
        ),
        migrations.AlterField(
            model_name='reply',
            name='comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reply_comments', to='posts.comment'),
        ),
        migrations.AlterField(
            model_name='reply',
            name='content',
            field=models.CharField(max_length=255),
        ),
    ]
