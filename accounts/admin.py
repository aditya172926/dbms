from django.contrib import admin
from accounts.models import UserProfile, Student, Faculty, Department, Course, Student_enroll, Research_Project, Researcher

# Register your models here.

admin.site.site_header = 'Admin'

class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user', 
        'Designation', 
        'Address',
        'phone',
        'Date_of_birth',
        'Gender',
        'Staff_id'
        )

    def get_queryset(self, request):
        queryset = super(UserProfileAdmin, self).get_queryset(request)
        queryset = queryset.order_by('phone', 'user')
        return queryset

class StudentProfileAdmin(admin.ModelAdmin):
    list_display = (
        'University_id',
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

class FacultyAdminProfile(admin.ModelAdmin):
    list_display = (
        'First_name',
        'Middle_name',
        'Last_name',
        'Gender',
        'Date_of_birth',
        'Phone_number',
        'Salary',
        'Grade',
        'Designation',
        'Age'
    )

class DepartmentAdminProfile(admin.ModelAdmin):
    list_display = (
        'Name',
        'HOD',
        'Phone',
        'email'
    )
    
class CourseAdminProfile(admin.ModelAdmin):
    list_display = (
        'Name',
        'Code',
        'Department'
    )

class ResearchProjectAdminProfile(admin.ModelAdmin):
    list_display = (
        'Faculty_id',
        'Name',
        'Area',
        'Duration'
    )

class ResearcherAdminProfile(admin.ModelAdmin):
    list_display = (
        'Faculty_id',
        'Project_id'
    )

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Student, StudentProfileAdmin)
admin.site.register(Faculty, FacultyAdminProfile)
admin.site.register(Department, DepartmentAdminProfile)
admin.site.register(Course, CourseAdminProfile)
admin.site.register(Student_enroll)
admin.site.register(Research_Project, ResearchProjectAdminProfile)
admin.site.register(Researcher, ResearcherAdminProfile)