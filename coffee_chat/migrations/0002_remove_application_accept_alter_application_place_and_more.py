# Generated by Django 4.1.3 on 2022-11-03 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffee_chat', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='accept',
        ),
        migrations.AlterField(
            model_name='application',
            name='place',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='application',
            name='target',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='application',
            name='time',
            field=models.CharField(default='', max_length=50),
        ),
    ]