# Generated by Django 3.0.3 on 2020-02-24 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='publication/pictures/', verbose_name='publication picture'),
        ),
    ]
