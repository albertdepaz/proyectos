# Generated by Django 3.0.3 on 2020-02-24 18:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200223_1759'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='like_taken',
        ),
    ]
