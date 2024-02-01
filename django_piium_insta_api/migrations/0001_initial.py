# Generated by Django 5.0.1 on 2024-01-11 16:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(null=True)),
                ('posts', models.TextField(null=True)),
                ('followers', models.TextField(null=True)),
                ('following', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.TextField(null=True)),
                ('like', models.TextField(null=True)),
                ('content', models.TextField(null=True)),
                ('tags', models.TextField(blank=True, null=True)),
                ('profile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post', to='django_piium_insta_api.profile')),
            ],
        ),
    ]
