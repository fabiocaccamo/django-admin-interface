import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("admin_interface", "0028_theme_show_fieldsets_as_tabs_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="theme",
            name="css_generic_link_active_color",
            field=colorfield.fields.ColorField(
                blank=True,
                default="#29B864",
                help_text="#29B864",
                image_field=None,
                max_length=10,
                samples=None,
                verbose_name="link active color",
            ),
        ),
    ]
