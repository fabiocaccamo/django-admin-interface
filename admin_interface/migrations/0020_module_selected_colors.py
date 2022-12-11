from __future__ import unicode_literals

import colorfield.fields
from django.db import migrations
from django.db.models import F


def default_link_selected(apps, schema_editor):
    Theme = apps.get_model("admin_interface", "Theme")
    db_alias = schema_editor.connection.alias
    Theme.objects.using(db_alias).update(
        css_module_link_selected_color=F("css_module_link_color")
    )


class Migration(migrations.Migration):

    dependencies = [
        ("admin_interface", "0019_add_form_sticky"),
    ]

    operations = [
        migrations.AddField(
            model_name="theme",
            name="css_module_background_selected_color",
            field=colorfield.fields.ColorField(
                blank=True,
                default="#FFFFCC",
                help_text="#FFFFCC",
                max_length=10,
                verbose_name="background selected color",
            ),
        ),
        migrations.AddField(
            model_name="theme",
            name="css_module_link_selected_color",
            field=colorfield.fields.ColorField(
                blank=True,
                default="#FFFFFF",
                help_text="#FFFFFF",
                max_length=10,
                verbose_name="link selected color",
            ),
        ),
        migrations.RunPython(default_link_selected),
    ]
