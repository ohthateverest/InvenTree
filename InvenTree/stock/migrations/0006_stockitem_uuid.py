# Generated by Django 2.2 on 2019-04-12 15:06

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0005_stockitemtracking_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='stockitem',
            name='uuid',
            field=models.UUIDField(blank=True, default=uuid.uuid4, editable=False),
        ),
    ]
