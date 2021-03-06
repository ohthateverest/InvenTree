# Generated by Django 2.2 on 2019-04-16 14:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('part', '0008_auto_20190417_0013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplierpart',
            name='part',
            field=models.ForeignKey(limit_choices_to={'purchaseable': True}, on_delete=django.db.models.deletion.CASCADE, related_name='supplier_parts', to='part.Part'),
        ),
    ]
