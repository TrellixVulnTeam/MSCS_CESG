# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-14 05:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booklease', '0010_auto_20161113_2359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_status',
            field=models.CharField(blank=True, choices=[('AV', 'Available'), ('OH', 'On Hold'), ('RE', 'Rented')], default='AV', max_length=2),
        ),
    ]
