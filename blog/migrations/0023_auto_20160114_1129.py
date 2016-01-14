# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0022_delete_clientbuild'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientBuild',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('buildusername', models.CharField(unique=True, max_length=45, verbose_name='Build Username')),
                ('buildpassword', models.CharField(unique=True, max_length=45, verbose_name='Build Password')),
            ],
        ),
        migrations.RemoveField(
            model_name='client',
            name='buildusername',
        ),
    ]
