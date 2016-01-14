# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_auto_20160113_1602'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='buildpassword',
            field=models.CharField(default=None, unique=True, max_length=45, verbose_name='Build Password'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='client',
            name='buildusername',
            field=models.CharField(default='None', unique=True, max_length=45, verbose_name='Build Username'),
            preserve_default=False,
        ),
    ]
