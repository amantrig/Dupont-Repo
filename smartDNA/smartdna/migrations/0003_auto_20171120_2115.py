# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smartdna', '0002_auto_20171120_2111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='asset_code',
            field=models.CharField(default=b'', max_length=32, verbose_name=b'Asset-ID', db_index=True),
        ),
        migrations.AlterUniqueTogether(
            name='registration',
            unique_together=set([('asset_code', 'status', 'scan_time')]),
        ),
    ]
