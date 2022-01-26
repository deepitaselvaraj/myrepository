from dataclasses import fields
from pyexpat import model
from django.forms import ModelForm
from .models import emp_det

class EmployeeForm(ModelForm):
    class Meta:
        model=emp_det
        fields='__all__'
        