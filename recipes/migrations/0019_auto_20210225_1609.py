# Generated by Django 3.1.2 on 2021-02-25 15:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0018_auto_20210225_1409'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rate',
            old_name='stars',
            new_name='score',
        ),
    ]