from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("admin_interface", "0024_remove_theme_css"),
    ]

    operations = [
        migrations.AddField(
            model_name="theme",
            name="language_chooser_control",
            field=models.CharField(
                choices=[
                    ("default-select", "Default Select"),
                    ("minimal-select", "Minimal Select"),
                ],
                default="default-select",
                max_length=20,
                verbose_name="control",
            ),
        ),
    ]
