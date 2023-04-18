from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("admin_interface", "0022_add_logo_max_width_and_height"),
    ]

    operations = [
        migrations.AddField(
            model_name="theme",
            name="foldable_apps",
            field=models.BooleanField(
                default=True,
                verbose_name="foldable apps",
            ),
        ),
    ]
