# Generated by Django 5.0.2 on 2024-03-25 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_alter_studentinfo_std_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentinfo',
            name='std_password',
            field=models.CharField(default='123456', editable=False, max_length=10),
        ),
        migrations.AlterField(
            model_name='studentinfo',
            name='std_id',
            field=models.CharField(editable=False, max_length=10, primary_key=True, serialize=False),
        ),
    ]
