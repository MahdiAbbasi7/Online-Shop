# Generated by Django 4.1.7 on 2023-05-18 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_module', '0003_slider'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='image',
            field=models.ImageField(upload_to='images/site-setting', verbose_name='تصویر اسلایدر'),
        ),
    ]
