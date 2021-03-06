# Generated by Django 3.0.5 on 2020-04-30 18:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tag', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventoRedZone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('portalName', models.CharField(max_length=15)),
                ('sentido', models.CharField(max_length=15)),
                ('temperature', models.IntegerField()),
                ('battery', models.IntegerField()),
                ('status', models.IntegerField()),
                ('timestamp', models.DateTimeField(blank=True, null=True)),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tag.Tag')),
            ],
        ),
    ]
