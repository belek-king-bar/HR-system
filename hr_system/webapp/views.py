from django.shortcuts import render, reverse
from webapp.models import EmployeeData
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from webapp.forms import EmployeeDataForm
from django.http import HttpResponseRedirect


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


class EmployeeDataCreateView(LoginRequiredMixin, CreateView):
    model = EmployeeData
    form_class = EmployeeDataForm
    template_name = 'employee_data_create.html'

    def get_success_url(self):
        return reverse('webapp:employee_list')

    def post(self, request, *args, **kwargs):
        form = EmployeeDataForm(request.POST)
        if form.is_valid():
            is_manager = request.POST.get('is_manager')
            if is_manager == 'on':
                is_manager = True
            else:
                is_manager = False
            EmployeeData.objects.create(
                employee=request.user,
                name=request.POST.get('name'),
                surname=request.POST.get('surname'),
                patronymic=request.POST.get('patronymic'),
                date_of_birth=request.POST.get('date_of_birth'),
                position=request.POST.get('position'),
                phone=request.POST.get('phone'),
                email=request.POST.get('email'),
                corporate_email=request.user.email,
                gitlab_account=request.POST.get('gitlab_account'),
                is_manager=is_manager,
                is_confirmed=True)
            success_url = self.get_success_url()
            return HttpResponseRedirect(success_url)
