# Generated by Django 5.0.1 on 2024-02-11 21:08

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_post_liked_by'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='bookmarks',
            field=models.ManyToManyField(related_name='favorite_posts', to=settings.AUTH_USER_MODEL),
        ),
    ]
