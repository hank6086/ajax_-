# Generated by Django 3.0 on 2020-01-02 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0008_auto_20191230_2022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='id_ap',
            name='idname',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='id_ap',
            name='uid',
            field=models.CharField(default='', max_length=50),
        ),
    ]
