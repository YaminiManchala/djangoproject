from django import forms
from .models import Job

class JobForm(forms.ModelForm):

    class Meta:
        model = Job
        fields = ['role', 'package', 'eligibility', 'location', 'job_mode']

        widgets = {
            'role': forms.TextInput(attrs={'class': 'form-input'}),
            'package': forms.NumberInput(attrs={'class': 'form-input'}),
            'eligibility': forms.TextInput(attrs={'class': 'form-input'}),
            'location': forms.TextInput(attrs={'class': 'form-input'}),
            'job_mode': forms.Select(
                choices=[
                    ('Onsite', 'Onsite'),
                    ('Remote', 'Remote'),
                    ('Hybrid', 'Hybrid')
                ],
                attrs={'class': 'form-input'}
            ),
        }