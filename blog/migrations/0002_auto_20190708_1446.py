# Generated by Django 2.2.3 on 2019-07-08 05:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='createdDate',
            new_name='created_date',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='publishedDate',
            new_name='published_date',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='textd',
            new_name='text',
        ),
    ]
