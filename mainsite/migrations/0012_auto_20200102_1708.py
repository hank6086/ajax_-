# Generated by Django 3.0 on 2020-01-02 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0011_auto_20200102_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='megall',
            name='meg_text',
            field=models.TextField(),
        ),
    ]
