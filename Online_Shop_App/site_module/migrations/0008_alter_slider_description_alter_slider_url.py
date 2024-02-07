# Generated by Django 4.1.7 on 2023-05-18 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_module', '0007_alter_slider_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='description',
            field=models.TextField(verbose_name='توضیحات اسلایدر'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='url',
            field=models.URLField(max_length=500, verbose_name='لینک'),
        ),
    ]