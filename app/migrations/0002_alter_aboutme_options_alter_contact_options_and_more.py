# Generated by Django 4.2.20 on 2025-04-12 08:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aboutme',
            options={'verbose_name': 'About me'},
        ),
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name': 'Contact'},
        ),
        migrations.AlterModelOptions(
            name='techtools',
            options={'verbose_name': 'Tech tool', 'verbose_name_plural': 'Tech tools'},
        ),
    ]
