# Generated by Django 2.2.2 on 2019-06-21 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('get_platform', '0004_auto_20190612_1056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='integratedplatforms',
            name='short_description',
            field=models.TextField(null=True),
        ),
    ]
