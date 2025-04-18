# Generated by Django 5.0.2 on 2024-02-28 22:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('project_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.project_model')),
            ],
        ),
    ]
