# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0033_auto_20160115_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientbuild',
            name='buildpassword',
            field=models.CharField(null=True, default=b'SOME STRING', max_length=45, blank=True, unique=True, verbose_name='Build Password'),
        ),
        migrations.AlterField(
            model_name='clientbuild',
            name='buildusername',
            field=models.CharField(null=True, default=b'SOME STRING', max_length=45, blank=True, unique=True, verbose_name='Build Username'),
        ),
    ]
