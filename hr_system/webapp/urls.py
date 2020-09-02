from django.urls import path
from webapp.views import EmployeeListView


app_name = 'webapp'


urlpatterns = [
    path('employees', EmployeeListView.as_view(), name='employee_list'),
]
