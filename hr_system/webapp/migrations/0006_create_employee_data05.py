from django.db import migrations, models


def create_employee_data(apps, schema_editor):
    employee = apps.get_model('webapp', 'Employee').objects.all().last()
    apps.get_model('webapp', 'EmployeeData').objects.create(employee=employee, name='Белек', surname='Тулибаев',
                                                            patronymic='Тилекбекович', date_of_birth='1995-10-17',
                                                            position='trainee', phone='996775190095',
                                                            email='belektolubaev@gmail.com',
                                                            corporate_email='belek@sunrisestudio.pro',
                                                            gitlab_account='gitlab.com/belek', is_active=True,
                                                            is_confirmed=True, is_manager=True)


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_creategroups05'),
    ]

    operations = [
        migrations.RunPython(create_employee_data),
    ]
