# Generated by Django 2.2.2 on 2019-06-12 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('get_platform', '0003_remove_integratedplatforms_courses'),
    ]

    operations = [
        migrations.AlterField(
            model_name='integratedplatforms',
            name='short_description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
