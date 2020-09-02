from django.shortcuts import render, reverse
from webapp.models import EmployeeData, Wage
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from webapp.forms import EmployeeDataForm, WageForm
from django.http import HttpResponseRedirect, JsonResponse
from datetime import datetime
from django.contrib.auth.models import Group


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
                group = Group.objects.get(name='Manager')
                request.user.groups.add(group)
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


class WagesView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Wage
    template_name = 'wages.html'
    permission_required = 'webapp.view_wage'
    permission_denied_message = 'Данный пользователь не имеет доступа к этой странице'

    def get(self, request, *args, **kwargs):
        date_month = self.request.GET.get('date__month')
        if date_month:
            wage_list = Wage.objects.filter(date__month=date_month)
        else:
            wage_list = Wage.objects.filter(date__month=datetime.now().month)
        return render(request, 'wages.html', context={'wage_list': wage_list})

    def post(self, *args, **kwargs):
        form = WageForm(self.request.POST)
        if form.is_valid():
            wage_id = self.request.POST.get('id')
            wage = Wage.objects.get(pk=wage_id)
            wage.salary = self.request.POST.get('salary')
            wage.prepaid = self.request.POST.get('prepaid')
            wage.prize = self.request.POST.get('prize')
            wage.issued = self.request.POST.get('issued')
            wage.save()
            response_wage = [{'wage': wage.salary}]
            return JsonResponse(response_wage, safe=False)
