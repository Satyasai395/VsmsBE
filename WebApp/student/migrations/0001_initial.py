# Generated by Django 5.0.2 on 2024-03-23 11:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CourseInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=20)),
                ('course_short_form', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='BatchInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch_name', models.CharField(max_length=100)),
                ('date_started', models.DateField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.courseinfo')),
            ],
        ),
        migrations.CreateModel(
            name='StudentInfo',
            fields=[
                ('std_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('std_full_name', models.CharField(max_length=50)),
                ('std_email', models.EmailField(max_length=254, unique=True)),
                ('std_phone_no', models.CharField(max_length=13)),
                ('std_address', models.TextField()),
                ('std_qualification', models.CharField(max_length=10)),
                ('std_year_of_passed_out', models.DateField()),
                ('std_gender', models.CharField(choices=[('male', 'Male'), ('Female', 'Female')], max_length=10)),
                ('std_img', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('batch_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='student.batchinfo')),
                ('course_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.courseinfo')),
            ],
            options={
                'unique_together': {('std_id', 'course_type')},
            },
        ),
    ]
