from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("admin_interface", "0023_theme_foldable_apps"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="theme",
            name="css",
        ),
    ]
