# Generated by Django 3.1 on 2021-03-01 08:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('generic', '0003_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='user',
        ),
    ]
