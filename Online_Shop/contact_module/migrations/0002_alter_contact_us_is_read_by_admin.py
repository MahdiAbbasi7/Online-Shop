# Generated by Django 4.1.7 on 2023-03-09 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_module', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact_us',
            name='is_read_by_admin',
            field=models.BooleanField(default='False', verbose_name='خوانده شده توسط ادمین'),
        ),
    ]
