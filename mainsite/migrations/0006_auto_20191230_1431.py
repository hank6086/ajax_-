# Generated by Django 3.0 on 2019-12-30 06:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0005_id_ap_ticket'),
    ]

    operations = [
        migrations.RenameField(
            model_name='id_ap',
            old_name='ticket',
            new_name='session',
        ),
    ]
