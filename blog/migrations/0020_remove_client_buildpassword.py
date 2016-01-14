# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_auto_20160113_1610'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='buildpassword',
        ),
    ]
