from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from accounts.forms import RegistrationForm, EditProfileForm, StudentUploadForm, FacultyUploadForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.email = form.cleaned_data['email']
            user.userprofile.phone = form.cleaned_data['phone']
            user.userprofile.Designation = form.cleaned_data['Designation']
            user.userprofile.Address = form.cleaned_data['Address']
            user.userprofile.Date_of_birth = form.cleaned_data['Date_of_birth']
            user.userprofile.Gender = form.cleaned_data['Gender']
            user.userprofile.Staff_id = form.cleaned_data['Staff_id']
            user.save()
            return redirect('/home')
    else:
        form = RegistrationForm()

    args = {'form': form}
    return render(request, 'accounts/reg_form.html', args)

def view_profile(request):
    args = {
        'user' : request.user
    }
    return render(request, 'accounts/profile.html', args)

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('/account/profile')
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'accounts/edit_profile.html', args)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/account/profile')
        else:
            return redirect('/account/change-password')
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'accounts/change_password.html', args)

class StudentUploadingForm(TemplateView):
    template_name = 'accounts/studentform.html'
    def get(self, request):
        form = StudentUploadForm()
        args = {
            'form': form
        }
        return render(request, self.template_name, args)
    def post(self, request):
        form = StudentUploadForm(request.POST)
        if form.is_valid():
            form.save()
            form = StudentUploadForm()
        args = {
            'form': form,
        }
        return render(request, self.template_name, args)

class FacultyRegisterForm(TemplateView):
    template_name = 'accounts/facultyform.html'
    def get(self, request):
        form = FacultyUploadForm()
        args = {
            'form': form,
        }
        return render(request, self.template_name, args)
    def post(self, request):
        form = FacultyUploadForm(request.POST)
        if form.is_valid():
            form.save()
            form = FacultyUploadForm()
        args = {
            'form': form,
        }
        return render(request, self.template_name, args)