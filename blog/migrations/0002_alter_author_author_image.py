# Generated by Django 4.0 on 2021-05-28 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='author_image',
            field=models.ImageField(upload_to='authors'),
        ),
    ]