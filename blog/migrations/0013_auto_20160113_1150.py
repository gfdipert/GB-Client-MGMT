# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20160112_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='appsub',
            field=models.DateTimeField(null=True, verbose_name='Apple Submitted', blank=True),
        ),
    ]
