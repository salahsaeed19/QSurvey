# Generated by Django 5.1.3 on 2024-12-04 08:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('responses', '0001_initial'),
        ('surveys', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='response',
            name='survey',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='responses', to='surveys.survey'),
        ),
    ]
