# Generated by Django 2.2.4 on 2019-09-08 13:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('one', '0005_auto_20190906_1705'),
    ]

    operations = [
        migrations.RenameField(
            model_name='setting',
            old_name='cookie_kashano',
            new_name='cookie',
        ),
        migrations.RenameField(
            model_name='setting',
            old_name='estates_kashano',
            new_name='estates',
        ),
        migrations.RenameField(
            model_name='setting',
            old_name='transactions_kashano',
            new_name='transactions',
        ),
    ]
