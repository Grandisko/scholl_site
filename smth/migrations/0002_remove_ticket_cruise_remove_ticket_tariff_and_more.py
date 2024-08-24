# Generated by Django 5.0.7 on 2024-08-05 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smth', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='cruise',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='tariff',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='user',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='status',
        ),
        migrations.RemoveField(
            model_name='tariff',
            name='type',
        ),
        migrations.AlterField(
            model_name='boat',
            name='name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='cruise',
            name='name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='tariff',
            name='name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.DeleteModel(
            name='Notification',
        ),
        migrations.DeleteModel(
            name='Ticket',
        ),
    ]