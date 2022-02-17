# Generated by Django 3.0.5 on 2020-04-29 17:00

import collaborator.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Collaborator',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=15)),
                ('last_name', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=70)),
                ('foto', models.FileField(blank=True, null=True, upload_to=collaborator.models.get_file_path)),
                ('statusAssociacao', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
