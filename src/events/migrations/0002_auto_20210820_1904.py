# Generated by Django 3.2.6 on 2021-08-20 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='email_address',
            field=models.EmailField(blank=True, max_length=254, verbose_name='Email Address'),
        ),
        migrations.AlterField(
            model_name='location',
            name='phone_number',
            field=models.CharField(blank=True, max_length=25, verbose_name='Contact Phone'),
        ),
        migrations.AlterField(
            model_name='location',
            name='web',
            field=models.URLField(blank=True, verbose_name='Website Address'),
        ),
    ]