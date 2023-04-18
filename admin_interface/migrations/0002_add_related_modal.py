import colorfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("admin_interface", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="theme",
            name="list_filter_dropdown",
            field=models.BooleanField(
                default=False,
                verbose_name="use dropdown",
            ),
        ),
        migrations.AddField(
            model_name="theme",
            name="related_modal_active",
            field=models.BooleanField(
                default=True,
                verbose_name="active",
            ),
        ),
        migrations.AddField(
            model_name="theme",
            name="related_modal_background_color",
            field=colorfield.fields.ColorField(
                blank=True,
                default="#000000",
                help_text="#000000",
                max_length=10,
                verbose_name="background color",
            ),
        ),
        migrations.AddField(
            model_name="theme",
            name="related_modal_background_opacity",
            field=models.FloatField(
                choices=[
                    (0.1, "10%"),
                    (0.2, "20%"),
                    (0.3, "30%"),
                    (0.4, "40%"),
                    (0.5, "50%"),
                    (0.6, "60%"),
                    (0.7, "70%"),
                    (0.8, "80%"),
                    (0.9, "90%"),
                ],
                default=0.2,
                help_text="20%",
                verbose_name="background opacity",
            ),
        ),
        migrations.AddField(
            model_name="theme",
            name="related_modal_rounded_corners",
            field=models.BooleanField(
                default=True,
                verbose_name="rounded corners",
            ),
        ),
    ]
