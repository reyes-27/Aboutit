# Generated by Django 4.1.3 on 2022-12-17 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0005_alter_post_repost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='repost',
            field=models.ManyToManyField(blank=True, null=True, to='social.post'),
        ),
    ]
