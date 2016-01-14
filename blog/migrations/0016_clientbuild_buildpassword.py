# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_clientbuild'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientbuild',
            name='buildpassword',
            field=models.CharField(default=None, unique=True, max_length=45, verbose_name='Build Password'),
            preserve_default=False,
        ),
    ]
