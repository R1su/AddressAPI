# Generated by Django 5.1.3 on 2024-11-05 15:26

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('city', models.CharField(max_length=100)),
                ('street', models.CharField(max_length=100)),
                ('building', models.CharField(max_length=20)),
            ],
        ),
    ]
