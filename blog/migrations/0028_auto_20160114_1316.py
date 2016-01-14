# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0027_client_buildusername'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientbuild',
            name='buildpassword',
            field=models.CharField(default=b'SOME STRING', unique=True, max_length=45, verbose_name='Build Password'),
        ),
        migrations.AlterField(
            model_name='clientbuild',
            name='buildusername',
            field=models.CharField(default=b'SOME STRING', unique=True, max_length=45, verbose_name='Build Username'),
        ),
    ]
