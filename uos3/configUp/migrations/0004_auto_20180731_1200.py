# Generated by Django 2.0.7 on 2018-07-31 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('configUp', '0003_auto_20180731_1145'),
    ]

    operations = [
        migrations.RenameField(
            model_name='config',
            old_name='confirm_uplink',
            new_name='confirmed_uplink',
        ),
    ]
