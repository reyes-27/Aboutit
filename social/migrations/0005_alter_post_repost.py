# Generated by Django 4.1.3 on 2022-12-17 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0004_remove_post_repost_post_repost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='repost',
            field=models.ManyToManyField(to='social.post'),
        ),
    ]