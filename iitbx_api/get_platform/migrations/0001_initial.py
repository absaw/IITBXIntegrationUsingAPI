# Generated by Django 2.2.1 on 2019-06-04 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IntegratedPlatforms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('org', models.TextField()),
                ('thirdparty_platform_name', models.TextField(null=True)),
                ('ServerUrl', models.TextField()),
                ('integrationstart', models.DateTimeField(null=True)),
                ('integrationend', models.DateTimeField(null=True)),
                ('isactive', models.BooleanField(default=False)),
                ('short_description', models.TextField(null=True)),
            ],
        ),
    ]
