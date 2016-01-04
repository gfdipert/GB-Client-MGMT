# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=45, verbose_name='Name')),
                ('gstatus', models.IntegerField(default=0, verbose_name='Guidebuilding Status', choices=[(0, b'New'), (1, b'Guidebuilding'), (2, b'Guidebuild Sufficient'), (3, b'Complete')])),
                ('pstatus', models.IntegerField(default=0, verbose_name='Google Play Status', choices=[(0, b'Not Submitted'), (1, b'Play Published')])),
                ('bstatus', models.IntegerField(default=0, verbose_name='Blackberry Status', choices=[(0, b'Not Submitted'), (1, b'Blackberry Published')])),
                ('astatus', models.IntegerField(default=0, verbose_name='Amazon Status', choices=[(0, b'Not Submitted'), (1, b'Amazon Published')])),
                ('intro', models.DateField(null=True, verbose_name='Intro Email Sent', blank=True)),
                ('appsub', models.DateField(null=True, verbose_name='Apple Submitted', blank=True)),
                ('apppub', models.DateField(null=True, verbose_name='Apple Published', blank=True)),
            ],
        ),
    ]
