# Generated by Django 5.1.4 on 2025-01-30 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='is_ended',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='event',
            name='status',
            field=models.CharField(choices=[('Ongoing', 'Sắp diễn ra'), ('Completed', 'Kết thúc')], default='Ongoing', max_length=10),
        ),
    ]
