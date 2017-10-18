# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-18 21:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        ('gesconweb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Permiso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_creacion', models.DateField(auto_now_add=True)),
                ('orden', models.IntegerField(default=0)),
                ('aplicativo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gesconweb.Aplicativo')),
                ('grupo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.Group')),
            ],
        ),
    ]
