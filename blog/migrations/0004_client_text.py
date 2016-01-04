# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20160104_1025'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='text',
            field=models.TextField(default=b'Some String'),
        ),
    ]
