# Generated by Django 4.0 on 2021-05-28 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_author_author_date_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='author_image',
            field=models.ImageField(height_field=130, upload_to='authors', width_field=131),
        ),
    ]
