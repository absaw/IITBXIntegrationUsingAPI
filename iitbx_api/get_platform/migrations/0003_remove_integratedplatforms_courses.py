# Generated by Django 2.2.1 on 2019-06-06 11:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('get_platform', '0002_integratedplatforms_courses'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='integratedplatforms',
            name='courses',
        ),
    ]
