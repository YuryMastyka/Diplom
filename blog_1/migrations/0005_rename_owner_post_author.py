# Generated by Django 4.0.6 on 2022-07-08 19:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_1', '0004_alter_post_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='owner',
            new_name='author',
        ),
    ]
