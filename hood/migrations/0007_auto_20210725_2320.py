# Generated by Django 3.2.5 on 2021-07-25 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0006_alter_neighborhood_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='neighborhood',
            name='health_department',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='neighborhood',
            name='police_department',
            field=models.TextField(blank=True, null=True),
        ),
    ]
