# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_auto_20160113_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientbuild',
            name='buildpassword',
            field=models.CharField(unique=True, max_length=45, verbose_name='Build Password'),
        ),
        migrations.AlterField(
            model_name='clientbuild',
            name='buildusername',
            field=models.CharField(unique=True, max_length=45, verbose_name='Build Username'),
        ),
    ]
