from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Student, Faculty

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required = True)
    Designation = forms.CharField(required=True)
    Address = forms.CharField(required=True)
    Date_of_birth = forms.CharField(required=True)
    Gender = forms.CharField(required=True)
    Staff_id = forms.CharField(required=True)
    phone = forms.IntegerField(required=True)

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'Designation',
            'Address',
            'Date_of_birth',
            'Gender',
            'Staff_id',
            'phone',
            'password1',
            'password2'
        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.phone = self.cleaned_data['phone']

        if commit:
            user.save()
        return user

class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name'
        )

class StudentUploadForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = (
            'First_name',
            'Middle_name',
            'Last_name',
            'Gender',
            'Date_of_birth',
            'Phone_number',
            'Address',
            'Course',
            'Department'
        )

class FacultyUploadForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = (
            'First_name',
            'Middle_name',
            'Last_name',
            'Gender',
            'Date_of_birth',
            'Phone_number',
            'Salary',
            'Grade',
            'Designation',
            'Course',
            'Department'
        )
        