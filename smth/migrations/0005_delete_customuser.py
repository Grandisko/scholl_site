# Generated by Django 5.0.7 on 2024-08-09 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smth', '0004_customuser'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]