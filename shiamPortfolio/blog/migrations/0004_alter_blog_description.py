# Generated by Django 3.2.8 on 2021-10-24 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_remove_blog_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='description',
            field=models.CharField(max_length=2000),
        ),
    ]
