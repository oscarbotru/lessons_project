from django import forms
from django.contrib.auth.forms import UserCreationForm

from funny.forms_mixins import StyleFormMixin
from funny.models import Student, Subject


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = '__all__'


class SubjectForm(forms.ModelForm):

    class Meta:
        model = Subject
        fields = '__all__'
