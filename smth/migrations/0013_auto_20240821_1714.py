# Generated by Django 5.0.7 on 2024-08-21 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smth', '0012_auto_20240821_1658'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='position',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
