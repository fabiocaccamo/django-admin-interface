from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("admin_interface", "0018_theme_list_filter_sticky"),
    ]

    operations = [
        migrations.AddField(
            model_name="theme",
            name="form_pagination_sticky",
            field=models.BooleanField(default=False, verbose_name="sticky pagination"),
        ),
        migrations.AddField(
            model_name="theme",
            name="form_submit_sticky",
            field=models.BooleanField(default=False, verbose_name="sticky submit"),
        ),
    ]
