# Generated by Django 5.0.1 on 2024-02-16 05:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_piium_insta_api', '0002_rename_profile_reels_profiles'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reels',
            old_name='profiles',
            new_name='profile',
        ),
    ]