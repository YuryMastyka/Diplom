# Generated by Django 4.0.6 on 2022-07-04 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default='default title', max_length=50),
            preserve_default=False,
        ),
    ]
