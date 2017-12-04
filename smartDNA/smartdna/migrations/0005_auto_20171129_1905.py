# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smartdna', '0004_auto_20171120_2119'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='registration',
            unique_together=set([('asset_code', 'status')]),
        ),
    ]
