import colorfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Theme",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        serialize=False,
                        auto_created=True,
                        primary_key=True,
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        default="Django",
                        max_length=50,
                    ),
                ),
                (
                    "active",
                    models.BooleanField(
                        default=True,
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        default="Django administration",
                        max_length=50,
                        blank=True,
                    ),
                ),
                (
                    "title_visible",
                    models.BooleanField(
                        default=True,
                        verbose_name="visible",
                    ),
                ),
                (
                    "logo",
                    models.FileField(
                        upload_to="admin-interface/logo/",
                        blank=True,
                    ),
                ),
                (
                    "logo_visible",
                    models.BooleanField(
                        default=True,
                        verbose_name="visible",
                    ),
                ),
                (
                    "css_header_background_color",
                    colorfield.fields.ColorField(
                        default="#0C4B33",
                        help_text="#0C4B33",
                        max_length=10,
                        verbose_name="background color",
                        blank=True,
                    ),
                ),
                (
                    "css_header_title_color",
                    colorfield.fields.ColorField(
                        default="#F5DD5D",
                        help_text="#F5DD5D",
                        max_length=10,
                        verbose_name="title color",
                        blank=True,
                    ),
                ),
                (
                    "css_header_text_color",
                    colorfield.fields.ColorField(
                        default="#44B78B",
                        help_text="#44B78B",
                        max_length=10,
                        verbose_name="text color",
                        blank=True,
                    ),
                ),
                (
                    "css_header_link_color",
                    colorfield.fields.ColorField(
                        default="#FFFFFF",
                        help_text="#FFFFFF",
                        max_length=10,
                        verbose_name="link color",
                        blank=True,
                    ),
                ),
                (
                    "css_header_link_hover_color",
                    colorfield.fields.ColorField(
                        default="#C9F0DD",
                        help_text="#C9F0DD",
                        max_length=10,
                        verbose_name="link hover color",
                        blank=True,
                    ),
                ),
                (
                    "css_module_background_color",
                    colorfield.fields.ColorField(
                        default="#44B78B",
                        help_text="#44B78B",
                        max_length=10,
                        verbose_name="background color",
                        blank=True,
                    ),
                ),
                (
                    "css_module_text_color",
                    colorfield.fields.ColorField(
                        default="#FFFFFF",
                        help_text="#FFFFFF",
                        max_length=10,
                        verbose_name="text color",
                        blank=True,
                    ),
                ),
                (
                    "css_module_link_color",
                    colorfield.fields.ColorField(
                        default="#FFFFFF",
                        help_text="#FFFFFF",
                        max_length=10,
                        verbose_name="link color",
                        blank=True,
                    ),
                ),
                (
                    "css_module_link_hover_color",
                    colorfield.fields.ColorField(
                        default="#C9F0DD",
                        help_text="#C9F0DD",
                        max_length=10,
                        verbose_name="link hover color",
                        blank=True,
                    ),
                ),
                (
                    "css_module_rounded_corners",
                    models.BooleanField(
                        default=True,
                        verbose_name="rounded corners",
                    ),
                ),
                (
                    "css_generic_link_color",
                    colorfield.fields.ColorField(
                        default="#0C3C26",
                        help_text="#0C3C26",
                        max_length=10,
                        verbose_name="link color",
                        blank=True,
                    ),
                ),
                (
                    "css_generic_link_hover_color",
                    colorfield.fields.ColorField(
                        default="#156641",
                        help_text="#156641",
                        max_length=10,
                        verbose_name="link hover color",
                        blank=True,
                    ),
                ),
                (
                    "css_save_button_background_color",
                    colorfield.fields.ColorField(
                        default="#0C4B33",
                        help_text="#0C4B33",
                        max_length=10,
                        verbose_name="background color",
                        blank=True,
                    ),
                ),
                (
                    "css_save_button_background_hover_color",
                    colorfield.fields.ColorField(
                        default="#0C3C26",
                        help_text="#0C3C26",
                        max_length=10,
                        verbose_name="background hover color",
                        blank=True,
                    ),
                ),
                (
                    "css_save_button_text_color",
                    colorfield.fields.ColorField(
                        default="#FFFFFF",
                        help_text="#FFFFFF",
                        max_length=10,
                        verbose_name="text color",
                        blank=True,
                    ),
                ),
                (
                    "css_delete_button_background_color",
                    colorfield.fields.ColorField(
                        default="#BA2121",
                        help_text="#BA2121",
                        max_length=10,
                        verbose_name="background color",
                        blank=True,
                    ),
                ),
                (
                    "css_delete_button_background_hover_color",
                    colorfield.fields.ColorField(
                        default="#A41515",
                        help_text="#A41515",
                        max_length=10,
                        verbose_name="background hover color",
                        blank=True,
                    ),
                ),
                (
                    "css_delete_button_text_color",
                    colorfield.fields.ColorField(
                        default="#FFFFFF",
                        help_text="#FFFFFF",
                        max_length=10,
                        verbose_name="text color",
                        blank=True,
                    ),
                ),
                (
                    "css",
                    models.TextField(
                        blank=True,
                    ),
                ),
                (
                    "list_filter_dropdown",
                    models.BooleanField(
                        default=False,
                    ),
                ),
            ],
            options={
                "verbose_name": "Theme",
                "verbose_name_plural": "Themes",
            },
        ),
    ]
