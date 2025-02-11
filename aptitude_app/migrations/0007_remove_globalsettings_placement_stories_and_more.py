# Generated by Django 5.1.4 on 2025-02-11 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aptitude_app', '0006_globalsettings_placement_stories'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='globalsettings',
            name='placement_stories',
        ),
        migrations.AddField(
            model_name='globalsettings',
            name='notice_board',
            field=models.TextField(default='Velammal', max_length=10000),
        ),
    ]
