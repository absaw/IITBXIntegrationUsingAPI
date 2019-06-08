# Generated by Django 2.2.1 on 2019-05-30 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CourseOverview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.IntegerField()),
                ('coursekey', models.TextField(max_length=255, null=True)),
                ('_location', models.TextField(max_length=255, null=True)),
                ('org', models.TextField()),
                ('display_name', models.TextField()),
                ('display_number_with_default', models.TextField()),
                ('display_org_with_default', models.TextField()),
                ('course_run', models.TextField(max_length=255)),
                ('start', models.DateTimeField(null=True)),
                ('end', models.DateTimeField(null=True)),
                ('advertised_start', models.TextField(null=True)),
                ('announcement', models.DateTimeField(null=True)),
                ('course_image_url', models.TextField(null=True)),
                ('social_sharing_url', models.TextField(null=True)),
                ('end_of_course_survey_url', models.TextField(null=True)),
                ('certificates_display_behavior', models.TextField(null=True)),
                ('certificates_show_before_end', models.BooleanField(default=False)),
                ('cert_html_view_enabled', models.BooleanField(default=False)),
                ('has_any_active_web_certificate', models.BooleanField(default=False)),
                ('cert_name_short', models.TextField(null=True)),
                ('cert_name_long', models.TextField(null=True)),
                ('lowest_passing_grade', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('days_early_for_beta', models.FloatField(null=True)),
                ('mobile_available', models.BooleanField(default=False)),
                ('visible_to_staff_only', models.BooleanField(default=False)),
                ('_pre_requisite_courses_json', models.TextField(null=True)),
                ('enrollment_start', models.DateTimeField(null=True)),
                ('enrollment_end', models.DateTimeField(null=True)),
                ('enrollment_domain', models.TextField(null=True)),
                ('invitation_only', models.BooleanField(default=False)),
                ('max_student_enrollments_allowed', models.IntegerField(null=True)),
                ('catalog_visibility', models.TextField(null=True)),
                ('short_description', models.TextField(null=True)),
                ('course_video_url', models.TextField(null=True)),
                ('effort', models.TextField(null=True)),
                ('self_paced', models.BooleanField(default=False)),
                ('marketing_url', models.TextField(null=True)),
                ('eligible_for_financial_aid', models.BooleanField(default=True)),
                ('language', models.TextField(null=True)),
                ('created_on_edx', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
