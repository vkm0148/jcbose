# Generated by Django 2.2.2 on 2019-07-08 20:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jcbose', '0005_auto_20190709_0208'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='Name_yourself',
            new_name='post',
        ),
    ]