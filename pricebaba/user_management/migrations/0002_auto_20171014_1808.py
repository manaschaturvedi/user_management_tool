# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-14 18:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricebaba_users',
            name='mobile',
            field=models.CharField(max_length=15),
        ),
    ]
