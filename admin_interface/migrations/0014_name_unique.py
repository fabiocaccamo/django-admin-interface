from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("admin_interface", "0013_add_related_modal_close_button"),
    ]

    operations = [
        migrations.AlterField(
            model_name="theme",
            name="name",
            field=models.CharField(
                default="Django", max_length=50, unique=True, verbose_name="name"
            ),
        ),
    ]
