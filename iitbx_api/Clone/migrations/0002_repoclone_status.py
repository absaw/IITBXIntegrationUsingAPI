# Generated by Django 2.2.1 on 2019-06-11 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clone', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='repoclone',
            name='status',
            field=models.TextField(blank=True),
        ),
    ]
