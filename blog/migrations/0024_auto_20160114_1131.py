# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0023_auto_20160114_1129'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ClientBuild',
        ),
        migrations.AddField(
            model_name='client',
            name='buildusername',
            field=models.CharField(default='X', unique=True, max_length=45, verbose_name='Build Username'),
            preserve_default=False,
        ),
    ]
