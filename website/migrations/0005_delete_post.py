# Generated by Django 4.2.14 on 2024-09-07 05:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_rename_created_at_post_created_time_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Post',
        ),
    ]
