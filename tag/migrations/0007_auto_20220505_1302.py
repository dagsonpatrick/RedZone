# Generated by Django 3.0.5 on 2022-05-05 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tag', '0006_auto_20220505_1254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='description',
            field=models.CharField(default='2022-05-05 23:33:33', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tag',
            name='temperature',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
