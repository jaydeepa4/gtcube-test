# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-07 16:39
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Question_Type', models.CharField(blank=True, default='', max_length=250)),
                ('Tags', models.TextField(blank=True, default='')),
                ('Para_Text', models.TextField(blank=True, default='')),
                ('Question_Text', models.TextField(blank=True, default='')),
                ('Options', models.TextField(blank=True, default='')),
                ('Answer_Option', models.CharField(blank=True, default='', max_length=250)),
                ('Solution', models.TextField(blank=True, default='')),
                ('Search_Tags', models.TextField(blank=True, default='')),
                ('Created_Time', models.DateTimeField(auto_now_add=True)),
                ('Updated_Time', models.DateTimeField(auto_now=True)),
                ('seller_obj', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
