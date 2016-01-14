# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0021_auto_20160113_1623'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ClientBuild',
        ),
    ]
