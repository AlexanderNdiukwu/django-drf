# Generated by Django 5.1.6 on 2025-03-12 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_todo_description_alter_todo_folder_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Variation',
            fields=[
                ('variation_id', models.AutoField(primary_key=True, serialize=False)),
                ('variation_value', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Variation_value',
            fields=[
                ('variation_value_id', models.AutoField(primary_key=True, serialize=False)),
                ('variation_value_value', models.CharField(max_length=15)),
            ],
        ),
        migrations.AlterField(
            model_name='folder',
            name='folder_description',
            field=models.TextField(max_length=600),
        ),
        migrations.AlterField(
            model_name='folder',
            name='folder_name',
            field=models.CharField(max_length=600),
        ),
        migrations.AlterField(
            model_name='status',
            name='status_input',
            field=models.CharField(choices=[('important', 'important'), ('not important', 'not important'), ('not sure', 'not sure')], default='not sure', max_length=600),
        ),
        migrations.AlterField(
            model_name='todo',
            name='description',
            field=models.TextField(max_length=600),
        ),
        migrations.AlterField(
            model_name='todo',
            name='title',
            field=models.CharField(max_length=600),
        ),
    ]
