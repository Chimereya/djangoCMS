# Generated by Django 5.0.1 on 2024-02-17 00:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_alter_bookmark_unique_together'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='author',
        ),
    ]
