# Generated by Django 3.1.2 on 2020-10-28 19:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('awward', '0006_delete_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
    ]