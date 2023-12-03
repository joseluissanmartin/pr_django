# Generated by Django 4.2.7 on 2023-12-03 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quimun', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quimun',
            old_name='content',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='quimun',
            name='title',
        ),
        migrations.AddField(
            model_name='quimun',
            name='rut',
            field=models.CharField(default='sin valor', max_length=10),
            preserve_default=False,
        ),
    ]
