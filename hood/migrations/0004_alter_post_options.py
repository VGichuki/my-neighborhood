# Generated by Django 3.2.5 on 2021-07-24 19:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0003_post'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-pk']},
        ),
    ]
