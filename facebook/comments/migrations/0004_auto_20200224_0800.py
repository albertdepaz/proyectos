# Generated by Django 3.0.3 on 2020-02-24 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0003_auto_20200224_0757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='comments/pictures/', verbose_name='comments picture'),
        ),
    ]