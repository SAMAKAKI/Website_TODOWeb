from django import forms
from .models import *

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control mb-5',
                'id': 'floatingInput',
                'placeholder': 'Project name',
            }),
        }


class TaskForm(forms.ModelForm):
    class Meta: 
        model = TODO
        fields = ['name', 'project']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control mb-5',
                'id': 'floatingInput',
                'placeholder': 'Task name',
            }),
            'project': forms.Select(attrs={
                'class': 'form-select',
                'id': 'floatingSelect',
                'placeholder': 'Select your project name'
            })
        }