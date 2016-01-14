# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0030_auto_20160114_1317'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='buildusername',
        ),
        migrations.AddField(
            model_name='client',
            name='buildappname',
            field=models.CharField(default=b'Some string', unique=True, max_length=45, verbose_name='Build App Name'),
        ),
    ]
