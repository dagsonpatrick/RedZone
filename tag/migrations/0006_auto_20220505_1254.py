# Generated by Django 3.0.5 on 2022-05-05 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tag', '0005_tagcore_status'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TagCore',
        ),
        migrations.RenameField(
            model_name='tag',
            old_name='address',
            new_name='uuid',
        ),
        migrations.AddField(
            model_name='tag',
            name='dateCreate',
            field=models.DateTimeField(auto_now_add=True, default='2022-05-05 11:41:45.008823'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tag',
            name='dateUpdate',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tag',
            name='status',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tag',
            name='battery',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tag',
            name='description',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
