# Generated by Django 2.1.8 on 2019-05-22 08:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20190522_0132'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='date_created',
            new_name='created_at',
        ),
    ]