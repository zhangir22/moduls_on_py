from .models import Employee
from django.forms import ModelForm, CharField, TextInput, Select, forms


class EmployeeUpdate(ModelForm):
    username = CharField(required=True)
    last_name = CharField(required=True)
    age = CharField(required=False)
    department = CharField(required=False)
    program_language = CharField(required=False)
    class Meta:
        model = Employee
        fields = "__all__"

        def save(self, commit=True):
            employee = super(forms.RegisterForm, self).save(commit=False)
            if commit:
                employee.save()
            return employee


class EmployeeForm(ModelForm):

    class Meta:
        model = Employee
        fields = ['name', 'last_name', 'age', 'department', 'program_language']
        widgets = {'name': TextInput(attrs={
            'class': 'form-control',
            'name': 'name',
            'id': 'name',
            'type':'text'

        }),
            'last_name': TextInput(attrs={
                'class': 'form-control',
                'name': 'last_name',
                'id': 'last_name',
                'type': 'text'

            }),
            'age': TextInput(attrs={
                'class': 'form-control',
                'name': 'age',
                'id': 'age',
                'type': 'number',
                'min': '18',
                'max': '70'

            }),
            'program_language': Select(attrs={
                'class': 'custom-select , form-control',
                'name': 'program-language',
                'id': 'program-language',


            }),
            'department': Select(attrs={
                'class': 'custom-select , form-control',
                'name': 'program-language',
                'id': 'program-language',
            }),
        }