from django.db import migrations, models


def create_groups(apps, schema_editor):
    apps.get_model('auth', 'Group').objects.create(name='Manager')
    apps.get_model('auth', 'Group').objects.create(name='Employee')


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_createusers05'),
    ]

    operations = [
        migrations.RunPython(create_groups),
    ]
