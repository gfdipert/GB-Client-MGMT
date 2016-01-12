# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20160106_1257'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.AddField(
            model_name='client',
            name='prostatus',
            field=models.IntegerField(default=0, verbose_name='Guidebuilding Service', choices=[(0, b'Pro'), (1, b'DIY')]),
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
