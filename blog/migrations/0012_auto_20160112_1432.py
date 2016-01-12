# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_client_apptype'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='eventdate',
            field=models.DateField(null=True, verbose_name='Event Date', blank=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='gstatus',
            field=models.IntegerField(default=0, verbose_name='Guidebuilding Status', choices=[(0, b'New - Guide Not Built'), (1, b'Guidebuilding'), (2, b'Guidebuild Sufficient for Submission'), (3, b'Complete')]),
        ),
    ]
