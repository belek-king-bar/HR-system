from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from webauth.managers import UserManager


class Employee(AbstractUser):
    username = None
    email = models.EmailField(max_length=254, unique=True, verbose_name=_('email address'))

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email


class EmployeeData(models.Model):
    POSITION_TRAINEE = 'trainee'
    POSITION_BACKEND = 'backend'
    POSITION_PM = 'pm'
    POSITION_FRONTEND = 'frontend'
    POSITION_IOS = 'ios'
    POSITION_ANDROID = 'android'

    POSITION_CHOICES = (
        (POSITION_TRAINEE, 'Стажер'),
        (POSITION_BACKEND, 'Бэкенд'),
        (POSITION_PM, 'ПМ'),
        (POSITION_FRONTEND, 'Фронтенд'),
        (POSITION_IOS, 'IOS'),
        (POSITION_ANDROID, 'Андроид')
    )

    employee = models.OneToOneField(Employee, on_delete=models.CASCADE, related_name='data',
                                    verbose_name='Пользователь')
    name = models.CharField(max_length=200, verbose_name='Имя')
    surname = models.CharField(max_length=200, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=200, null=True, blank=True, verbose_name='Отчество')
    date_of_birth = models.DateField(verbose_name='Дата рождения')
    position = models.CharField(max_length=30, default=POSITION_TRAINEE, verbose_name='Позиция',
                                choices=POSITION_CHOICES)
    phone = models.CharField(max_length=20, verbose_name='Телефон номер')
    email = models.EmailField(max_length=254, verbose_name='Личный email')
    corporate_email = models.EmailField(max_length=254, verbose_name='Корпоративный email')
    gitlab_account = models.CharField(max_length=200, verbose_name='Gitlab аккаунт')
    created_at = models.DateTimeField(auto_now_add=True)
    is_fired = models.BooleanField(default=False, verbose_name='Статус что сотрудник уволен')
    is_active = models.BooleanField(default=False, verbose_name='Активен ли сотрудник')
    is_confirmed = models.BooleanField(default=False, verbose_name='Подтвержден ли сотрудник')
    is_manager = models.BooleanField(default=False, verbose_name='Менеджер ли сотрудник')

    def __str__(self):
        return "%s %s - %s" % (self.name, self.surname, self.position)


class Wage(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE, related_name='wage', verbose_name='Сотрудник')
    salary = models.IntegerField(default=0, verbose_name='Оклад')
    prepaid = models.IntegerField(default=0, verbose_name='Аванс')
    prize = models.IntegerField(default=0, verbose_name='Премия')
    issued = models.CharField(max_length=30, default='Нет', verbose_name='Выдано?')
    date = models.DateField(verbose_name='Месяц')

    def __str__(self):
        return "%s %s - %s" % (self.employee, self.salary, self.date)

