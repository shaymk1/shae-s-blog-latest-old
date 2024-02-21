# Generated by Django 5.0.2 on 2024-02-21 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author_image',
            field=models.ImageField(blank=True, default='placeholder.png', null=True, upload_to='articles'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='placeholder.png', null=True, upload_to='articles'),
        ),
    ]
