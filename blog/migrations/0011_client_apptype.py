# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20160112_1406'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='apptype',
            field=models.IntegerField(default=0, verbose_name='App Type', choices=[(0, b'GB Premium'), (1, b'Standalone'), (2, b'Multiguide')]),
        ),
    ]
