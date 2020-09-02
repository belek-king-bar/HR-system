from django.shortcuts import render
from webapp.models import EmployeeData
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin


class EmployeeListView(LoginRequiredMixin, ListView):
    model = EmployeeData
    template_name = 'employee.html'

    def get(self, request, *args, **kwargs):
        is_active = self.request.GET.get('is_active')
        is_fired = self.request.GET.get('is_fired')
        position = self.request.GET.get('position')
        if is_active:
            employee_data_list = EmployeeData.objects.filter(is_active=True)
        elif is_fired:
            employee_data_list = EmployeeData.objects.filter(is_fired=True)
        elif position:
            employee_data_list = EmployeeData.objects.filter(position=position)
        else:
            employee_data_list = EmployeeData.objects.all()
        return render(request, 'employee.html', context={'employeedata_list': employee_data_list})
