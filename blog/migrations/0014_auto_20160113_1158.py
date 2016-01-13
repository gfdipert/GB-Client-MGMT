# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20160113_1150'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='checkapp',
            field=models.DateField(null=True, verbose_name='Check Apple Submission', blank=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='appsub',
            field=models.DateField(null=True, verbose_name='Apple Submitted', blank=True),
        ),
    ]
