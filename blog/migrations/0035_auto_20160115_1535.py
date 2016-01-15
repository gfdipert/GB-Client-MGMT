# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0034_auto_20160115_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientbuild',
            name='buildpassword',
            field=models.CharField(default=b'Password', unique=True, max_length=45, verbose_name='Build Password'),
        ),
        migrations.AlterField(
            model_name='clientbuild',
            name='buildusername',
            field=models.CharField(default=b'Username', unique=True, max_length=45, verbose_name='Build Username'),
        ),
    ]
