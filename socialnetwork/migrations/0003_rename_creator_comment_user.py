# Generated by Django 4.0.2 on 2022-03-07 23:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('socialnetwork', '0002_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='creator',
            new_name='user',
        ),
    ]