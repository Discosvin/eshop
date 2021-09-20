# Generated by Django 3.2.7 on 2021-09-17 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0017_auto_20210917_1609'),
    ]

    operations = [
        migrations.AddField(
            model_name='addon',
            name='slug',
            field=models.SlugField(default='2', max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default='1', max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='0', max_length=256, null=True),
        ),
    ]
