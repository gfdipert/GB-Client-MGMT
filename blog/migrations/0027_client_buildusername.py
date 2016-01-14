# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0026_remove_client_buildusername'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='buildusername',
            field=models.CharField(default=b'SOME STRING', unique=True, max_length=45, verbose_name='Build Username'),
        ),
    ]
