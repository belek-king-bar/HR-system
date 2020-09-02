from django.db import migrations, models


def create_wage(apps, schema_editor):
    employee = apps.get_model('webapp', 'Employee').objects.all().last()
    apps.get_model('webapp', 'Wage').objects.create(employee=employee, salary=20000, date='2020-09-01')


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_create_employee_data05'),
    ]

    operations = [
        migrations.RunPython(create_wage),
    ]
