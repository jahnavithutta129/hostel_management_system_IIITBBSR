# Generated by Django 5.0.6 on 2024-07-17 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_cloakroomsettings_cloakroomentry'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='facultyprofile',
            name='profile_image',
        ),
        migrations.RemoveField(
            model_name='studentprofile',
            name='profile_image',
        ),
    ]
