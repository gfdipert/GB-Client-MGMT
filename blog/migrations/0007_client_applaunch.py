# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20160104_1033'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='applaunch',
            field=models.DateField(null=True, verbose_name='Apple Launch Date', blank=True),
        ),
    ]
