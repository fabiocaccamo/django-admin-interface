# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("admin_interface", "0006_bytes_to_str"),
    ]

    operations = [
        migrations.AddField(
            model_name="theme",
            name="favicon",
            field=models.FileField(
                blank=True,
                help_text="(.ico|.png|.gif - 16x16|32x32 px)",
                upload_to="admin-interface/favicon/",
                verbose_name="favicon",
            ),
        ),
    ]
