# Generated by Django 5.0.1 on 2024-02-19 21:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_rename_followed_user_follow_following_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='follow',
            unique_together=set(),
        ),
    ]
