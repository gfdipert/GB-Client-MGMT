# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_client_text'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='text',
            new_name='guides',
        ),
    ]
