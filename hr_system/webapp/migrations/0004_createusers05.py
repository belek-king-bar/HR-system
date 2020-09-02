from django.db import migrations, models


def create_superuser(apps, schema_editor):
    apps.get_model('webapp', 'Employee').objects.create(email='admin@sunrisestudio.pro', password='admin',
                                                        is_staff=True, is_superuser=True)


def create_user(apps, schema_editor):
    apps.get_model('webapp', 'Employee').objects.create(email='belek@sunrisestudio.pro', password='7325real2342',
                                                        is_active=True)


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_wage'),
    ]

    operations = [
        migrations.RunPython(create_superuser),
        migrations.RunPython(create_user),
    ]
