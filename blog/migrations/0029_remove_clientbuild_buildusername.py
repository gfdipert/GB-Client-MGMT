# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0028_auto_20160114_1316'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientbuild',
            name='buildusername',
        ),
    ]
