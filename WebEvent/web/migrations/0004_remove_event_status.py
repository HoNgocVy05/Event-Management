# Generated by Django 5.1.4 on 2025-01-30 03:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_event_is_ended_alter_event_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='status',
        ),
    ]
