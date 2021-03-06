# Generated by Django 3.1.1 on 2020-09-02 13:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_employeedata'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salary', models.IntegerField(default=0, verbose_name='Оклад')),
                ('prepaid', models.IntegerField(default=0, verbose_name='Аванс')),
                ('prize', models.IntegerField(default=0, verbose_name='Премия')),
                ('issued', models.CharField(default='Нет', max_length=30, verbose_name='Выдано?')),
                ('date', models.DateField(verbose_name='Месяц')),
                ('employee', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='wage', to=settings.AUTH_USER_MODEL, verbose_name='Сотрудник')),
            ],
        ),
    ]
