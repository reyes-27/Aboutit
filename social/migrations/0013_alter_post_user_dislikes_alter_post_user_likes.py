# Generated by Django 4.1.3 on 2022-12-28 05:38

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('social', '0012_alter_category_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='user_dislikes',
            field=models.ManyToManyField(blank=True, related_name='user_dislikes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='user_likes',
            field=models.ManyToManyField(blank=True, related_name='user_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
