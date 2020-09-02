from django import forms
from webapp.models import EmployeeData, Wage


class EmployeeDataForm(forms.ModelForm):
    class Meta:
        model = EmployeeData
        exclude = ['employee', 'corporate_email', 'is_active', 'is_confirmed', 'is_fired', 'is_manager']


class WageForm(forms.ModelForm):
    class Meta:
        model = Wage
        fields = ['id', 'salary', 'prepaid', 'prize', 'issued']
