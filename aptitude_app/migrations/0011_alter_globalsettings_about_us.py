# Generated by Django 5.1.4 on 2025-02-11 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aptitude_app', '0010_merge_20250211_2327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='globalsettings',
            name='about_us',
            field=models.TextField(default='Velammal', max_length=10000),
        ),
    ]
