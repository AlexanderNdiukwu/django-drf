# Generated by Django 5.1.6 on 2025-03-11 00:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('folder_id', models.AutoField(primary_key=True, serialize=False)),
                ('folder_name', models.CharField(max_length=120)),
                ('folder_description', models.TextField(max_length=120)),
                ('folder_created_at', models.DateTimeField(auto_now_add=True)),
                ('folder_updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('status_id', models.AutoField(primary_key=True, serialize=False)),
                ('status_input', models.CharField(choices=[('important', 'important'), ('not important', 'not important'), ('not sure', 'not sure')], default='not sure', max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('completed', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('folder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.folder')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.status')),
            ],
        ),
    ]
