from django.db import migrations

from immunity_users.migrations import update_admins_permissions


class Migration(migrations.Migration):

    dependencies = [('immunity_users', '0007_unique_email')]

    operations = [
        migrations.RunPython(
            update_admins_permissions, reverse_code=migrations.RunPython.noop
        )
    ]
