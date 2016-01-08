# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20160104_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='appstatus',
            field=models.IntegerField(default=0, verbose_name='Apple Submission Status', choices=[(0, b'Pending Assets'), (1, b'Mockups Sent'), (2, b'Screenshots Sent'), (3, b'Apple Submitted'), (4, b'Apple Published')]),
        ),
    ]
