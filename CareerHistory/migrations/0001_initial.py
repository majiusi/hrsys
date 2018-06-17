# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-16 01:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CareerHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.TextField(max_length=200, verbose_name='会社名前')),
                ('start_date', models.DateField(verbose_name='開始日付')),
                ('end_date', models.DateField(verbose_name='終了日付')),
                ('role', models.CharField(max_length=100, verbose_name='役割')),
                ('department', models.TextField(max_length=200, verbose_name='部')),
                ('contribution', models.TextField(max_length=200, verbose_name='業務内容')),
            ],
            options={
                'verbose_name': '職務経歴',
                'verbose_name_plural': '職務経歴',
                'db_table': 'yo_career_history',
            },
        ),
    ]
