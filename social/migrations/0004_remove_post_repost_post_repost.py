# Generated by Django 4.1.3 on 2022-12-17 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0003_post_dislikes_post_user_dislikes_alter_like_post_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='repost',
        ),
        migrations.AddField(
            model_name='post',
            name='repost',
            field=models.ManyToManyField(blank=True, null=True, related_name='post_child', to='social.post'),
        ),
    ]
