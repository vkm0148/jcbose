# Generated by Django 2.2.2 on 2019-07-10 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jcbose', '0009_auto_20190710_2103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='Mobile_no',
            field=models.IntegerField(default=0),
        ),
    ]
