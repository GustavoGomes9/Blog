# Generated by Django 4.0 on 2021-05-28 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_author_altura_author_largura_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='altura',
        ),
        migrations.RemoveField(
            model_name='author',
            name='largura',
        ),
        migrations.AlterField(
            model_name='author',
            name='author_image',
            field=models.ImageField(upload_to='authors'),
        ),
    ]
