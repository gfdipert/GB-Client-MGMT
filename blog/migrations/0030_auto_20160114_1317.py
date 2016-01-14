# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0029_remove_clientbuild_buildusername'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='buildusername',
            field=models.CharField(default=b'SOME STRING', max_length=45, unique=True, null=True, verbose_name='Build Username'),
        ),
        migrations.AlterField(
            model_name='clientbuild',
            name='buildpassword',
            field=models.CharField(default=b'SOME STRING', max_length=45, unique=True, null=True, verbose_name='Build Password'),
        ),
    ]
