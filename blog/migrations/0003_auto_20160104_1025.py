# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_client'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='appstatus',
            field=models.IntegerField(default=0, verbose_name='Apple Store Status', choices=[(0, b'Pending Assets'), (1, b'Mockups Sent'), (2, b'Screenshots Sent'), (3, b'Apple Submitted'), (4, b'Apple Published')]),
        ),
        migrations.AlterField(
            model_name='client',
            name='astatus',
            field=models.IntegerField(default=0, verbose_name='Amazon Status', choices=[(0, b'Not Submitted'), (1, b'Submitted'), (2, b'Amazon Published')]),
        ),
        migrations.AlterField(
            model_name='client',
            name='bstatus',
            field=models.IntegerField(default=0, verbose_name='Blackberry Status', choices=[(0, b'Not Submitted'), (1, b'Submitted'), (2, b'Blackberry Published')]),
        ),
        migrations.AlterField(
            model_name='client',
            name='pstatus',
            field=models.IntegerField(default=0, verbose_name='Google Play Status', choices=[(0, b'Not Submitted'), (1, b'Submitted'), (2, b'Play Published')]),
        ),
    ]
