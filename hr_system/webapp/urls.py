from django.urls import path
from webapp.views import EmployeeListView, EmployeeDataCreateView, WagesView


app_name = 'webapp'


urlpatterns = [
    path('employees', EmployeeListView.as_view(), name='employee_list'),
    path('employee_data_create', EmployeeDataCreateView.as_view(), name='employee_data_create'),
    path('wages', WagesView.as_view(), name='wages'),
]
