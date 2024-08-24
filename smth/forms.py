from django import forms
from .models import Application, Question

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ('name', 'email', 'phone', 'student_name', 'student_class', 'passport_data', 'parent_name', 'parent_passport_data', 'files')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 100%;'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'style': 'width: 100%;'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 100%;'}),
            'student_name': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 100%;'}),
            'student_class': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 100%;'}),
            'passport_data': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 100%;'}),
            'parent_name': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 100%;'}),
            'parent_passport_data': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 100%;'}),
            'files': forms.FileInput(attrs={'class': 'form-control-file'}),
        }

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('text', 'email')
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control', 'style': 'width: 100%;'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'style': 'width: 100%;'}),
        }